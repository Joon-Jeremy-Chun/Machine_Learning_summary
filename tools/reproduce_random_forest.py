"""Execute the published Iris reference unchanged in an isolated Jupyter kernel.

This is bounded reproduction/operational verification, not a new model comparison.
The bootstrap option installs the reviewed lock into a new venv only.
"""
import argparse
import copy
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'python_machine_learning'/'Random_Forest.ipynb'
PACKAGES = ['pandas', 'scikit-learn', 'numpy', 'scipy', 'nbclient', 'nbformat', 'ipykernel']


def bootstrap(args):
    environment = args.venv_path.resolve()
    if environment.exists():
        raise RuntimeError('Choose a new --venv-path; an existing environment will not be overwritten.')
    lock = ROOT/'requirements-random-forest.lock.txt'
    if not lock.exists():
        raise RuntimeError('The reviewed random-forest lock is missing.')
    subprocess.run([sys.executable, '-m', 'venv', str(environment)], check=True)
    python = environment/('Scripts/python.exe' if sys.platform == 'win32' else 'bin/python')
    subprocess.run([str(python), '-m', 'pip', '--isolated', 'install',
                    '--index-url', 'https://pypi.org/simple', '--disable-pip-version-check',
                    '-r', str(lock)], check=True)
    subprocess.run([str(python), '-m', 'pip', 'check'], check=True)
    command = [str(python), str(Path(__file__).resolve()),
               '--output-dir', str(args.output_dir.resolve())]
    if args.reference:
        command.extend(['--reference', str(args.reference.resolve())])
    subprocess.run(command, cwd=ROOT, check=True)


def execute(args):
    if sys.prefix == sys.base_prefix:
        raise RuntimeError('Use an isolated virtual environment, or --bootstrap with a new path.')
    # Notebook execution dependencies are imported only after the bootstrap path.
    import nbformat
    from nbclient import NotebookClient
    from jupyter_client import KernelManager
    from jupyter_client.kernelspec import KernelSpecManager

    original = SOURCE.read_bytes()
    notebook = nbformat.reads(original.decode('utf-8-sig'), as_version=4)
    source_cells = [c['source'] for c in notebook.cells if c['cell_type'] == 'code']
    if len(source_cells) != 1:
        raise RuntimeError('Review the notebook again before changing the one-cell reproduction contract.')
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix='iris-notebook-') as folder:
        temporary = Path(folder)
        spec_base = temporary/'kernels'
        spec = spec_base/'portfolio-rf'
        spec.mkdir(parents=True)
        (spec/'kernel.json').write_text(json.dumps({
            'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
            'display_name': 'Isolated Iris reproduction', 'language': 'python',
        }), encoding='utf-8')
        manager = KernelManager(kernel_name='portfolio-rf',
                                kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(spec_base)]))
        run_directory = temporary/'work'
        run_directory.mkdir()
        metrics_path = run_directory/'metrics.json'
        # This diagnostic cell is removed from the saved executed notebook.
        expected_interpreter = hashlib.sha256(str(Path(sys.executable).resolve()).encode()).hexdigest()
        probe = '''
import hashlib, json, sys
from pathlib import Path
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
report = {
    "kernel_matches_requested_interpreter": hashlib.sha256(str(Path(sys.executable).resolve()).encode()).hexdigest() == EXPECTED,
    "kernel_is_virtual_environment": sys.prefix != sys.base_prefix,
    "train_rows": len(X_train), "test_rows": len(X_test),
    "classes": iris.target_names.tolist(),
    "train_class_counts": y_train.value_counts().sort_index().tolist(),
    "test_class_counts": y_test.value_counts().sort_index().tolist(),
    "split_overlap": len(set(X_train.index) & set(X_test.index)),
    "trees": model.n_estimators, "max_depth": model.max_depth,
    "seed": model.random_state, "jobs": model.n_jobs,
    "accuracy": float(accuracy_score(y_test, predicted)),
    "confusion_matrix": confusion_matrix(y_test, predicted, labels=model.classes_).tolist(),
    "classification_report": classification_report(y_test, predicted, target_names=iris.target_names, output_dict=True, zero_division=0),
    "importance": {str(k): float(v) for k, v in importance.items()},
    "test_indices": X_test.index.tolist(), "target": y_test.tolist(),
    "predicted": np.asarray(predicted).tolist(),
}
Path("metrics.json").write_text(json.dumps(report, sort_keys=True), encoding="utf-8")
'''.replace('EXPECTED', repr(expected_interpreter))
        execution = copy.deepcopy(notebook)
        execution.cells.append(nbformat.v4.new_code_cell(probe))
        client = NotebookClient(execution, km=manager, timeout=180,
                                resources={'metadata': {'path': str(run_directory)}})
        environment = dict(os.environ, PYTHONNOUSERSITE='1', PYTHONUTF8='1')
        environment.pop('PYTHONPATH', None)
        environment.pop('PYTHONHOME', None)
        try:
            client.execute(cwd=str(run_directory), env=environment)
            result = json.loads(metrics_path.read_text(encoding='utf-8'))
        finally:
            if manager.has_kernel:
                manager.shutdown_kernel(now=True)
            if client.kc is not None:
                client.kc.stop_channels()
        execution.cells.pop()
    assert result['kernel_matches_requested_interpreter']
    assert result['kernel_is_virtual_environment']
    assert (result['train_rows'], result['test_rows'], result['split_overlap']) == (105, 45, 0)
    assert result['train_class_counts'] == [35, 35, 35]
    assert result['test_class_counts'] == [15, 15, 15]
    assert (result['trees'], result['max_depth'], result['seed'], result['jobs']) == (200, 4, 2045, 1)
    assert abs(sum(result['importance'].values())-1) < 1e-10
    assert result['accuracy'] > .8  # Existing maintenance acceptance check, not a tuned target.
    assert SOURCE.read_bytes() == original
    assert [c['source'] for c in execution.cells if c['cell_type'] == 'code'] == source_cells
    stdout = ''.join(o.get('text', '') for c in execution.cells if c['cell_type'] == 'code'
                     for o in c.get('outputs', []) if o.get('output_type') == 'stream')
    source_sha = hashlib.sha256(original).hexdigest()
    result.update({
        'record_class': 'operational-verification',
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'python': sys.version.split()[0], 'platform': sys.platform,
        'source': 'python_machine_learning/Random_Forest.ipynb',
        'source_sha256': source_sha, 'source_unchanged': True,
        'source_text_lf_sha256': hashlib.sha256(original.replace(b'\r\n', b'\n')).hexdigest(),
        'source_hash_scope': 'execution checkout bytes; LF-normalized hash supports CRLF/LF comparison',
        'packages': {name: importlib.metadata.version(name) for name in PACKAGES},
        'existing_acceptance_accuracy_exclusive_minimum': .8,
        'elapsed_execution_seconds': round(time.monotonic()-started, 3),
        'all_passed': True,
        'limits': ['one existing fixed split; no model selection or comparison',
                   'package installation requires public PyPI; the Iris execution uses bundled data',
                   'this does not reproduce the external-data notebooks'],
    })
    # Stable public output fingerprint, independent of time, path and platform labels.
    stable = {k: result[k] for k in ['train_rows', 'test_rows', 'classes', 'trees', 'max_depth',
                                   'seed', 'accuracy', 'confusion_matrix', 'test_indices', 'target', 'predicted']}
    if args.reference:
        expected = json.loads(args.reference.read_text(encoding='utf-8'))
        assert stable == expected, 'The locked reproduction differs from the reviewed output fingerprint.'
    result['reference_matched'] = True if args.reference else None
    # Save success evidence only after every requested check has passed.
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    (output/'result.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    (output/'stdout.txt').write_text(stdout, encoding='utf-8')
    nbformat.write(execution, output/'executed.ipynb')
    (output/'prediction-fingerprint.json').write_text(json.dumps(stable, sort_keys=True, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'source_unchanged': True, 'train_rows': result['train_rows'],
                      'test_rows': result['test_rows'], 'accuracy': result['accuracy'],
                      'kernel_is_isolated': True, 'all_passed': True}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bootstrap', action='store_true')
    parser.add_argument('--venv-path', type=Path, default=ROOT/'.venv')
    parser.add_argument('--output-dir', type=Path,
                        default=ROOT/'outputs'/'random-forest-reproduction'/
                        datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    parser.add_argument('--reference', type=Path, help='Optional reviewed prediction fingerprint to match.')
    args = parser.parse_args()
    if args.bootstrap:
        bootstrap(args)
    else:
        execute(args)


if __name__ == '__main__':
    main()
