# Notebook cell catalog

Primary notebooks are listed below; six checkpoint copies remain preserved. Cell numbers are one-based positions. New notes are appended, so earlier cell numbers are unchanged.

## Linear regression from explicit gradients

[Detailed source map](notebooks/gradient-descent/README.md) · [Notebook](../python_machine_learning/Gradient_Descent.ipynb)

28 code cells. Give the loss-recording functions separate names so later definitions preserve the earlier two-value API. The Korean companion retains the historical unpacking failure; this longer version has no saved error output.

## A compact gradient-descent study

[Detailed source map](notebooks/gradient-descent-notes/README.md) · [Notebook](../python_machine_learning/Gradient_Descent%28%EA%B2%BD%EC%82%AC%ED%95%98%EA%B0%95%29.ipynb)

27 code cells. Give the loss-recording functions separate names so later definitions preserve the earlier two-value API. The Korean companion retains the historical unpacking failure; this longer version has no saved error output.

## Iris decision tree without Graphviz

[Detailed source map](notebooks/decision-tree/README.md) · [Notebook](../python_machine_learning/Decision_Tree.ipynb)

12 code cells. Use offline Iris, stratify the 70/30 split, derive plot labels from estimator.classes_, replace the missing Graphviz executable path with sklearn/Matplotlib plot_tree, and add a held-out report. Saved Graphviz failure remains historical.

## Complete an offline random-forest reference

[Detailed source map](notebooks/random-forest/README.md) · [Notebook](../python_machine_learning/Random_Forest.ipynb)

1 code cells. Complete the empty notebook with an offline stratified Iris random-forest example, held-out reporting and feature importances. This is explicitly new 2026 reference work, not a historical experiment.

## Bike demand: EDA and two OLS specifications

[Detailed source map](notebooks/bike-demand/README.md) · [Notebook](../python_machine_learning/Mini_project_Kaggle_Bike_Sharing_Demand_Modeling.ipynb)

42 code cells. Select the count target by bracket indexing (DataFrame.count is a method), import NumPy explicitly, and replace deprecated seaborn distplot calls with histplot. Casual/registered are retained for early EDA but removed in cell 48 before the OLS models. Random holdout remains an exploratory benchmark, not a chronological forecasting protocol.

## Rare-event detection with full and shallow trees

[Detailed source map](notebooks/fraud-trees/README.md) · [Notebook](../python_machine_learning/Mini_project_Kaggle_Fraud_Detection_Modeling.ipynb)

31 code cells. Use plot_tree without Graphviz, visualize the actual depth-limited Model_pr in the pruning section, and pass explicit x/y keywords to seaborn barplot. Showing only five levels of the unpruned tree does not itself prune the estimator.
