# Validation record — 2026-10-20

- Focused suite: 6 passed in 3.52 seconds; five expected noninteractive plotting warnings.
- Both bike OLS specifications and metric cells ran on synthetic data; actual built-in Iris tree/forest examples ran offline.
- Historical notebook output objects, counts, IDs and metadata matched the original state.
- Static critical checks and local document references were checked separately. Full external-data experiment reproduction was not attempted.

## Environment observed

| Package | Installed version |
|---|---|
| numpy | 2.1.3 |
| pandas | 2.2.3 |
| scikit-learn | 1.8.0 |
| matplotlib | 3.10.0 |
| seaborn | 0.13.2 |
| statsmodels | 0.15.0 |
| patsy | 1.0.3 |
| pytest | 9.1.1 |

Statsmodels/patsy were installed in an isolated temporary directory after the initial missing-dependency failure. Other packages came from the existing Windows environment. This is not a tested clean-install lockfile.

Root and the representative bike-demand guide were rendered locally and visually inspected.
