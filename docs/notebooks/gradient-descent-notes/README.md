# A compact gradient-descent study

[← Portfolio](../../../README.md) · [Open notebook](../../../python_machine_learning/Gradient_Descent%28%EA%B2%BD%EC%82%AC%ED%95%98%EA%B0%95%29.ipynb)

> Source repaired in 2026. Earlier outputs remain historical; focused checks are recorded separately.

## Question

Follow a shorter Korean working version of the linear-regression exercise.

## Data and access

The same embedded arrays and external testData.csv as the longer companion, with the read in cell 17.

## Method and pipeline

A two-parameter linear model, MSE derivatives and iterative updates precede a loss-history section. The two-value and three-value function interfaces now have separate names.

## Read the source

| Cell | Opening statement |
|---|---|
| 3 | `import warnings` |
| 5 | `def Machine(x, w, b):` |
| 6 | `x = np.array([1,3,5,7,9])` |
| 7 | `Machine(x, w, b)` |
| 8 | `def Gradient(x,y,w,b):` |
| 9 | `y = np.array([2,4,6,8,10])` |
| 10 | `print('dw is ', dw)` |
| 12 | `def Learning(x,y,w,b,step):` |
| 13 | `step = 0.05` |
| 14 | `print('Updated_w is ', '%.3f' % uw)` |
| 16 | `import pandas as pd` |
| 17 | `url = 'https://raw.githubusercontent.com/rusita-ai/pyData/master/testData.csv'` |
| 18 | `DATA.info()` |
| 19 | `DATA.head()` |
| 20 | `plt.scatter(DATA.inputs, DATA.outputs, s = 0.5)` |
| 21 | `w = 2` |
| 22 | `for i in range(0, 1500):` |
| 23 | `print('Learned_w is ', '%.3f' % w)` |
| 24 | `X = np.linspace(0, 1, 100)` |
| 26 | `def Gradient_with_loss(x, y, w, b):` |
| 27 | `def Learning_with_loss(x, y, w, b, step):` |
| 28 | `w = 2` |
| 29 | `for i in range(0, 1500):` |
| 30 | `Error[0:10]` |
| 31 | `plt.plot(Error)` |
| 32 | `plt.plot(Error[0:50], '.')` |
| 33 | `plt.plot(Error[1450:1500], '.')` |

Read preprocessing before fitting, then compare the evaluation target and predictions. Later cells may reuse the same model/data objects. Restart the kernel before a clean full run.

## Results and evidence

The saved ValueError remains visible. Fresh tests run all function definitions together and verify that the two-value API still works, loss-recording returns three values, and a known line is recovered.

## Limitations

Cell 22 stores an unpacking error consistent with a later three-value function definition being active. A clean top-to-bottom source read alone does not prove that historical execution order. The two notebooks are related learning versions, not independent experiments.

## Execution and dependencies

**Imports observed:** `matplotlib.pyplot`, `numpy`, `pandas`, `warnings`.

Read the [reproduction guide](../../REPRODUCIBILITY.md) before execution. Inspect network, Colab mount and unzip cells. External-data versions and the original environment are not locked.

## Attribution

The original notebook header credits the MultiCampus Data Science lectures. Exact original dates and individual/team contribution remain unverified.
