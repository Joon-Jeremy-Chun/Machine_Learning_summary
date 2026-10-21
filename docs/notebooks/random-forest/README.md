# Complete an offline random-forest reference

[← Portfolio](../../../README.md) · [Open notebook](../../../python_machine_learning/Random_Forest.ipynb)

> Source repaired in 2026. Earlier outputs remain historical; focused checks are recorded separately.

## Question

Extend a single decision tree into a reproducible ensemble exercise.

## Data and access

Built-in scikit-learn Iris; no files or network access are required. Stratified split: 105 training and 45 test rows.

## Method and pipeline

The newly completed cell trains 200 trees with max_depth=4, random_state=2045 and n_jobs=1. It prints a confusion matrix, per-class report and sorted impurity-based feature importances.

## Read the source

| Cell | Opening statement |
|---|---|
| 1 | `# New 2026 reference implementation completing the former empty notebook.` |

Read preprocessing before fitting, then compare the evaluation target and predictions. Later cells may reuse the same model/data objects. Restart the kernel before a clean full run.

## Results and evidence

A fresh focused check executes the entire completed cell, verifies test size and normalized importance, and checks useful held-out predictions. No historical score existed to preserve or compare.

## Limitations

The notebook was previously empty. This is new 2026 reference code, not restored historical research. One split and impurity importance do not establish superiority, causality or feature stability.

## Execution and dependencies

**Imports observed:** `pandas`, `sklearn.datasets`, `sklearn.ensemble`, `sklearn.metrics`, `sklearn.model_selection`.

Read the [reproduction guide](../../REPRODUCIBILITY.md) before execution. Inspect network, Colab mount and unzip cells. External-data versions and the original environment are not locked.

## Attribution

Original content was an empty notebook. The complete example is explicitly new maintenance reference work from 2026.
