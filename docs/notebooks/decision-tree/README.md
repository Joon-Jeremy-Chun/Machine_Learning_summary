# Iris decision tree without Graphviz

[← Portfolio](../../../README.md) · [Open notebook](../../../python_machine_learning/Decision_Tree.ipynb)

> Source repaired in 2026. Earlier outputs remain historical; focused checks are recorded separately.

## Question

Inspect an interpretable multiclass classifier and evaluate it on held-out Iris observations.

## Data and access

Offline scikit-learn Iris: 150 rows, four measurements and three species, rebuilt as a named DataFrame. Original code loaded seaborn Iris instead.

## Method and pipeline

A stratified 70%/30% split with random_state=2045 feeds DecisionTreeClassifier. plot_tree derives class names from estimator.classes_ and feature names from the DataFrame, followed by a confusion matrix and classification report.

## Read the source

| Cell | Opening statement |
|---|---|
| 2 | `import warnings` |
| 3 | `# Offline built-in Iris data; preserve the feature/species DataFrame layout.` |
| 4 | `DF.info()` |
| 5 | `DF.head()` |
| 6 | `DF.species.value_counts()` |
| 7 | `import matplotlib.pyplot as plt` |
| 8 | `X = DF[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]` |
| 9 | `from sklearn.model_selection import train_test_split` |
| 10 | `from sklearn.tree import DecisionTreeClassifier` |
| 11 | `from sklearn.tree import plot_tree` |
| 12 | `# Matplotlib avoids requiring the external Graphviz dot executable.` |
| 13 | `from sklearn.metrics import classification_report, confusion_matrix` |

Read preprocessing before fitting, then compare the evaluation target and predictions. Later cells may reuse the same model/data objects. Restart the kernel before a clean full run.

## Results and evidence

Historical cell 12 contains ExecutableNotFound. A fresh offline check trains the actual revised tree, renders its structure with a noninteractive backend, and checks the held-out predictions; saved notebook output is unchanged.

## Limitations

The former export supplied versicolor/virginica labels in the wrong order and failed because the external dot executable was missing. The revised Matplotlib path avoids that executable. This is still a single small holdout.

## Execution and dependencies

**Imports observed:** `matplotlib.pyplot`, `pandas`, `seaborn`, `sklearn.datasets`, `sklearn.metrics`, `sklearn.model_selection`, `sklearn.tree`, `warnings`.

Read the [reproduction guide](../../REPRODUCIBILITY.md) before execution. Inspect network, Colab mount and unzip cells. External-data versions and the original environment are not locked.

## Attribution

The original notebook header credits the MultiCampus Data Science lectures. Exact original dates and individual/team contribution remain unverified.
