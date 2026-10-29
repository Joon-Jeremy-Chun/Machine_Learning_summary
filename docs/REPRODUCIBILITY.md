# Reproduction guide

## Environment

Use Python/Jupyter with NumPy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, patsy, IPython and pytest. `requirements-validation.txt` is an unpinned dependency group for maintenance checks, not an original lockfile. Existing Windows packages plus an isolated statsmodels/patsy installation passed the focused checks; the selected offline random-forest reference now has a [clean-install reproduction path](reproduction/random-forest/README.md). Clean execution of the other full notebooks remains unverified.

```bash
python -m venv .venv
# Activate the virtual environment for your shell.
python -m pip install -r requirements-validation.txt
python -m pytest tests/test_notebook_repairs.py -q
python tools/validate_archive.py
```

## Inputs and effects

| Notebook | Data | Execution considerations |
|---|---|---|
| Two gradient-descent versions | Embedded arrays + remote testData.csv | Network read; inputs/outputs columns required; two 1,500-step sections. |
| Decision tree | Built-in Iris | Offline load, plotting and held-out report; no Graphviz binary required. |
| Random forest | Built-in Iris | Offline; 200 shallow trees, no output file writes. |
| Bike demand | Remote Bike_Sharing_Demand.csv | Network read, EDA/plots and two formula OLS fits; preserve raw count and component roles. |
| Fraud trees | External creditCardFraud.zip → creditcard.csv | Colab Drive mount/unzip; two fits on the supplied data. ZIP/data are not bundled. |

Remote CSV versions and original data redistribution terms are not fully recorded. The original Kaggle URLs remain in the notebooks. Adapt Colab paths to a prepared runtime rather than blindly executing shell cells locally.

## Evaluation and interpretation

The classifiers use one 70/30 split; revised Iris classifiers stratify with seed 2045. The fraud notebook deliberately compares unstratified and stratified splitting before fitting, and compares full/depth-5 trees on a shared holdout. Bike OLS uses a random 70/30 split, so it is not an out-of-time forecast. Its RMSE has units of rental counts; no new full-data value is reported. Gradient examples fit data in-sample to illustrate optimization.

## Historical output

Saved errors and results were preserved byte-for-byte at the output-object level. The new source can therefore appear above an old error/result. Read the appended maintenance note and detailed guide. Checkpoint notebooks remain original historical copies, not synchronized alternate entry points.

## Selected clean reference — 2026-10-29

Use the [Iris reproduction guide](reproduction/random-forest/README.md) for a new locked Python 3.11 venv and actual notebook kernel. Its runtime lock is separate from requirements-validation.txt and does not restore the external-data archive. Original notebook files/outputs are preserved; fresh execution artifacts have their own dated directory.
