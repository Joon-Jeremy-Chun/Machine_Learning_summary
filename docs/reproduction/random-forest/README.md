# Reproduce the Iris random-forest notebook

[Portfolio](../../../README.md) · [한국어](README.ko.md) · [Original notebook](../../../python_machine_learning/Random_Forest.ipynb)

This is a bounded installation/execution check of the **existing 2026 reference**. It is not new research, a model comparison, a parameter search, or reproduction of the external-data notebooks. The original notebook is executed unchanged in a fresh Jupyter kernel using built-in Iris data.

## Start from a new environment

Use Python 3.11 and run from the repository root:

```console
python tools/reproduce_random_forest.py --bootstrap --reference docs/reproduction/random-forest/2026-10-29/prediction-fingerprint.json
```

The helper creates a new `.venv`, installs pinned dependencies from public PyPI (45 Windows runtime packages plus two conditional Linux entries), runs `pip check`, and starts a kernel using that environment's exact Python executable. Installation needs internet; execution uses packaged Iris data. No external CSV, credential, Graphviz binary or GPU is needed. If `.venv` exists, choose a new `--venv-path` instead of overwriting it.

Fresh results go to a dated ignored `outputs/random-forest-reproduction/` folder. Optional `--output-dir` chooses another evidence location. `--reference` compares predictions and split indices against the reviewed output. Do not use this bootstrap to change the full historical environment.

For a prepared venv, run its Python directly:

```console
python tools/reproduce_random_forest.py --reference docs/reproduction/random-forest/2026-10-29/prediction-fingerprint.json
```

## What is verified

| Contract | Check |
| --- | --- |
| Source preservation | Original notebook SHA-256 and code cells unchanged |
| Actual environment | Kernel executable matches the requested venv |
| Split | 105 train / 45 test; class counts 35/15 each; zero overlapping indices |
| Existing parameters | 200 trees, depth 4, seed 2045, n_jobs=1 |
| Output | Existing accuracy acceptance >0.8, normalized feature importance, reviewed prediction fingerprint |
| Saved evidence | Executed notebook, stdout, environment/version metadata and stable fingerprint |

The command reads only this reviewed notebook, and executes it in an empty temporary working directory. Probe cells are removed from the saved notebook. No kernel connection file, private filesystem location or runtime address is included in public evidence.

Source byte hashes describe the execution checkout. LF-normalized hashes are recorded separately because Git can check out CRLF on Windows and LF on Linux.

## Observed output — 2026-10-29

![Confusion matrix from the fixed Iris split](confusion.svg)

The fixed split has 42 correct predictions out of 45 (93.33%); three virginica observations are predicted as versicolor. This is a fresh execution result on that split, not an historical course score or a claim of model superiority. The acceptance threshold was inherited from the earlier maintenance test, not selected after this run.

- [Executed notebook](2026-10-29/executed.ipynb)
- [Result and environment](2026-10-29/result.json)
- [Printed output](2026-10-29/stdout.txt)
- [Stable prediction fingerprint](2026-10-29/prediction-fingerprint.json)
- [Runtime version lock](../../../requirements-random-forest.lock.txt)

## Continuous verification and limits

The [workflow](../../../.github/workflows/random-forest-reproduction.yml) creates new locked venvs on Linux and Windows with Python 3.11, repeats the whole notebook and compares the reviewed output. Hosted results are confirmed separately from local execution.

A fixed version set does not pin the operating system, Python micro-version or package wheels by hash. One stratified split and impurity importance do not establish generalization stability or causality. No additional model variants, new evaluation protocol, real-world cohort or performance benchmark was introduced. These are operational reproduction records under the owner's simple-record policy, not a new research experiment.

References: [NBClient execution API](https://nbclient.readthedocs.io/en/latest/client.html), [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).
