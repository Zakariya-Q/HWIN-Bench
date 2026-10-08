# CI Calculation Verification — Run B (Canonical)

**Date**: 2026-10-08 (v1.0.4 rebuild)
**Canonical run**: `benchmark/results/grqa_recomputation/` (Run B, 2026-08-06/07)
**Scope**: all 11 variables x 7 models x 5 metrics = 385 combinations

---

## Methodology

The canonical Run-B artifacts record 25 fold-level evaluations per
model-variable-metric: 5 deterministic repetitions x 5 GroupKFold folds.
The 5 repetitions are computationally identical (the seed variable is never
consumed by any stochastic operation), so only **5 unique fold evaluations**
exist for uncertainty estimation.

- CI sample size: **n = 5**
- Degrees of freedom: **df = 4**
- t critical (95%): **2.7764451051977987**
- CI basis: the first repetition block (`all_values[:5]`), i.e. the unique folds

Point estimates are unchanged: the 5 identical repetitions share the same
mean, so mean(25 values) == mean(5 unique values) exactly (verified to 1e-12
for all 385 combinations).

## Two independent verification methods

- **Method A**: direct t-interval formula — mean +/- t * sem(unique)
- **Method B**: `scipy.stats.t.interval(0.95, df=4, loc=mean, scale=sem)`

Both methods were applied to all 385 combinations. The recomputed values were
also compared against the stored (repaired) `ci_95` in the canonical JSONs.

| Check | Combinations | Max absolute difference | Required |
|-------|--------------|--------------------------|----------|
| Method A vs Method B | 385 | 9.095e-13 | <= 1e-12 |
| Recomputed vs stored ci_95 | 385 | 9.095e-13 | <= 1e-12 |

**All 385 combinations pass.**

## Example (HWIN-VAR-001, extra_trees, r2)

- Recorded evaluations: 25 (5 repetitions x 5 folds)
- Unique fold values: [0.23762671898040466, 0.35753964709848607, 0.8030374851303783, 0.8043807879945226, 0.8214831503362005]
- Mean: 0.6048135579079985
- Corrected 95% CI (n=5, df=4): [0.25250243212638696, 0.9571246836896099]

## Provenance

- Canonical results: `benchmark/results/grqa_recomputation/all_results.json` and
  the 11 per-variable `HWIN-VAR-*_results.json` files
- Run A (`grqa_full_final_groupkfold`, 2026-07-08/09) is **historical**: it
  stored aggregated means only (no fold values), carried different point
  estimates, and was removed from the repository in maintenance release 1.0.3
- No full benchmark rerun was required or performed: the corrected CIs are
  recomputed directly from the stored Run-B fold values
