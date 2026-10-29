<div align="center">

![Machine learning learning archive](assets/readme/cover.svg)

# Machine Learning Summary

**An inspectable path from explicit gradients to decision trees, ensembles and applied metrics.**

[Reading path](#reading-path) · [Notebook guides](#notebook-guides) · [Reproduce](docs/REPRODUCIBILITY.md) · [Repairs](docs/REPAIRS.md)

</div>

Six primary notebooks preserve MultiCampus learning material on optimization and classical machine learning. The guides explain what each example computes, where its data come from, which cells to inspect and what the recorded outputs can support. Six checkpoint copies are retained as history.

> **Maintenance status — 2026-10-20:** all six primary notebooks were inspected and repaired; the empty random-forest notebook is now a clearly labeled reference implementation. Six focused tests passed. Existing outputs and error traces remain unchanged.

## Reading path

| Stage | Read first | What to compare |
|---|---|---|
| 1 · Optimization | [Gradient derivation](docs/notebooks/gradient-descent/README.md), then [compact notes](docs/notebooks/gradient-descent-notes/README.md) | Objective, derivatives, update size and persistent notebook state. |
| 2 · Classifiers | [Decision tree](docs/notebooks/decision-tree/README.md), then [random forest](docs/notebooks/random-forest/README.md) | A single partitioning rule versus an ensemble; class ordering and held-out evidence. |
| 3 · Applied evaluation | [Bike demand](docs/notebooks/bike-demand/README.md), then [fraud trees](docs/notebooks/fraud-trees/README.md) | Regression target/units, class imbalance, leakage and the limits of one split. |

## Notebook guides

| Investigation | Source |
|---|---|
| [Linear regression from explicit gradients](docs/notebooks/gradient-descent/README.md) | [Gradient_Descent.ipynb](python_machine_learning/Gradient_Descent.ipynb) |
| [A compact gradient-descent study](docs/notebooks/gradient-descent-notes/README.md) | [Gradient_Descent(경사하강).ipynb](python_machine_learning/Gradient_Descent%28%EA%B2%BD%EC%82%AC%ED%95%98%EA%B0%95%29.ipynb) |
| [Iris decision tree without Graphviz](docs/notebooks/decision-tree/README.md) | [Decision_Tree.ipynb](python_machine_learning/Decision_Tree.ipynb) |
| [Complete an offline random-forest reference](docs/notebooks/random-forest/README.md) | [Random_Forest.ipynb](python_machine_learning/Random_Forest.ipynb) |
| [Bike demand: EDA and two OLS specifications](docs/notebooks/bike-demand/README.md) | [Mini_project_Kaggle_Bike_Sharing_Demand_Modeling.ipynb](python_machine_learning/Mini_project_Kaggle_Bike_Sharing_Demand_Modeling.ipynb) |
| [Rare-event detection with full and shallow trees](docs/notebooks/fraud-trees/README.md) | [Mini_project_Kaggle_Fraud_Detection_Modeling.ipynb](python_machine_learning/Mini_project_Kaggle_Fraud_Detection_Modeling.ipynb) |

## Results worth reading carefully

| Saved evidence | Definition / source | What it supports |
|---|---|---|
| Full fraud tree: precision 0.78947, recall 0.81081 | Positive class 1; notebook cell 41 | Historical rare-event tradeoff on the watched 30% holdout. |
| Depth-5 fraud tree: precision 0.89130, recall 0.83108 | Positive class 1; cell 50 | A descriptive comparison; no independent model-selection validation. |
| Bike metric cells contain errors | Cells 55/59 used DataFrame.count | Fixed target access; there is no verified original RMSE to advertise. |
| Empty random-forest notebook | Original one-cell source | New reference implementation; no invented historical result. |

## Setup and verification

The decision-tree and new random-forest examples use offline built-in Iris data. Gradient/bike notebooks read external raw CSVs; fraud mounts and unzips a user-supplied Drive dataset. Follow the [dataset/environment guide](docs/REPRODUCIBILITY.md) before a full run.

```bash
python -m pip install -r requirements-validation.txt
python -m pytest tests/test_notebook_repairs.py -q
python tools/validate_archive.py
```

The focused suite checks gradients against known mathematics, the completed offline classifiers, the real OLS formulas/metric cells on synthetic data, and corrected plot behavior. It does not reproduce a Kaggle ranking or full-data fraud experiment.

## More detail

- [Cell catalog](docs/NOTEBOOK_CATALOG.md) and [collection index](python_machine_learning/README.md).
- [Repair log](docs/REPAIRS.md), [validation record](docs/VALIDATION.md), [figure provenance](assets/readme/SOURCES.md).
- [Korean maintenance handoff](docs/handoffs/HANDOFF_2026-10-20.md).
- Continue into [Deep Learning Summary](https://github.com/Joon-Jeremy-Chun/Deep_Learning_summary) for neural-network examples.

## Credits and scope

Original headers credit MultiCampus Data Science lectures. This is an educational archive. Exact original dates, personal/team roles and dataset versions remain unverified. New 2026 maintenance work is distinguished from historical material; no new license or deployment claim is assigned.

## Start with a fully executed offline reference

The [Iris random-forest reproduction](docs/reproduction/random-forest/README.md) installs a new locked Python 3.11 environment and executes the original notebook unchanged in an isolated Jupyter kernel. [한국어 안내](docs/reproduction/random-forest/README.ko.md). The [workflow](.github/workflows/random-forest-reproduction.yml) repeats the selected reference on Linux/Windows; it does not run the external-data notebook archive.
