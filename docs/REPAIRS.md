# Repairs and verification

Existing outputs, execution counts, IDs and cell metadata are preserved. Notes were appended after the original cells. All cell numbers below are one-based.

| Notebook | Edited cells | Repair |
|---|---|---|
| [Gradient_Descent.ipynb](../python_machine_learning/Gradient_Descent.ipynb) | 40, 42, 45 | Give the loss-recording functions separate names so later definitions preserve the earlier two-value API. The Korean companion retains the historical unpacking failure; this longer version has no saved error output. |
| [Gradient_Descent(경사하강).ipynb](../python_machine_learning/Gradient_Descent%28%EA%B2%BD%EC%82%AC%ED%95%98%EA%B0%95%29.ipynb) | 26, 27, 29 | Give the loss-recording functions separate names so later definitions preserve the earlier two-value API. The Korean companion retains the historical unpacking failure; this longer version has no saved error output. |
| [Decision_Tree.ipynb](../python_machine_learning/Decision_Tree.ipynb) | 3, 9, 11, 12, 13 | Use offline Iris, stratify the 70/30 split, derive plot labels from estimator.classes_, replace the missing Graphviz executable path with sklearn/Matplotlib plot_tree, and add a held-out report. Saved Graphviz failure remains historical. |
| [Mini_project_Kaggle_Bike_Sharing_Demand_Modeling.ipynb](../python_machine_learning/Mini_project_Kaggle_Bike_Sharing_Demand_Modeling.ipynb) | 18, 55, 59, 19, 22, 28, 30, 33, 36 | Select the count target by bracket indexing (DataFrame.count is a method), import NumPy explicitly, and replace deprecated seaborn distplot calls with histplot. Casual/registered are retained for early EDA but removed in cell 48 before the OLS models. Random holdout remains an exploratory benchmark, not a chronological forecasting protocol. |
| [Mini_project_Kaggle_Fraud_Detection_Modeling.ipynb](../python_machine_learning/Mini_project_Kaggle_Fraud_Detection_Modeling.ipynb) | 36, 37, 47, 44, 52 | Use plot_tree without Graphviz, visualize the actual depth-limited Model_pr in the pruning section, and pass explicit x/y keywords to seaborn barplot. Showing only five levels of the unpruned tree does not itself prune the estimator. |
| [Random_Forest.ipynb](../python_machine_learning/Random_Forest.ipynb) | 1 | Complete the empty notebook with an offline stratified Iris random-forest example, held-out reporting and feature importances. This is explicitly new 2026 reference work, not a historical experiment. |

## Verification boundary

Six focused cases exercise two gradient implementations, an actual offline decision-tree pipeline, the entire new random-forest cell, both bike OLS formulas and corrected RMSE targets on synthetic data, and fraud plotting with the correct estimator/modern seaborn calls. Figures use the Agg backend; they are not written over archived figures.

The first test attempt passed five cases but could not import statsmodels for OLS. statsmodels and patsy were installed in an isolated temporary tools directory; the suite was then rerun. Full external datasets, Kaggle submissions and all archived experiment outputs were not reproduced.

## Primary references

- [scikit-learn plot_tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html) — Matplotlib tree diagrams.
- [seaborn histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html) — explicit histogram interface.
- [statsmodels installation](https://www.statsmodels.org/stable/install.html) — OLS environment prerequisites.
