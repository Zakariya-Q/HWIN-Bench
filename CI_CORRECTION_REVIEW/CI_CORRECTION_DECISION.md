# CI CORRECTION DECISION — HWIN-Bench v1.0

**Date**: 2026-08-09  
**Final Verdict**: **CI CORRECTION ONLY** — All five unique fold-level values are recoverable. No model rerun required. Only CI statistics need recomputation.

---

## Answers to Required Questions

### 1. Were the five seed repetitions actually different?
**NO.** The five seed repetitions (42, 123, 256, 512, 1024) produced **computationally identical** GroupKFold partitions and model randomness. The outer `seed` variable is bound by the loop but **never referenced** in any stochastic operation (sampling, GroupKFold, model initialization). The five "repetitions" are five identical computations.

### 2. How many unique fold evaluations exist?
**5 unique fold evaluations** per variable-model combination. The 25 reported values (5 seeds × 5 folds) are **5 unique fold values repeated 5 times identically**.

### 3. Are the current 25-observation CIs statistically defensible?
**NO.** The current CIs treat 25 values as independent observations (n=25), but only 5 unique fold evaluations exist. This underestimates standard error by factor √5 and uses incorrect t-distribution degrees of freedom (df=24 vs df=4).

### 4. What should n be?
**n = 5** (the number of unique GroupKFold partitions). The protocol's "5 seeds × 5 folds = 25 evaluations" assumption is violated because seeds don't produce different folds.

### 5. Do point estimates change?
**NO.** The mean R², RMSE, MAE, MAPE, MedAE values remain **mathematically identical**. The mean of 25 identical repetitions equals the mean of the 5 unique values.

### 6. Which reported CIs change?
**ALL 385 CIs** (11 variables × 7 models × 5 metrics) change. All are widened by factor **3.0081** (≈3× wider). The corrected CIs use n=5, df=4, t=2.776 instead of n=25, df=24, t=2.064.

### 7. Is model training required again?
**NO.** All predictive point estimates remain valid. Only CI arithmetic needs recomputation.

### 8. What exact files must eventually be regenerated?
**Target files for correction:**
- `GRQA_full_benchmark_complete.json` (all 385 metric CIs)
- 11 per-variable JSON files (e.g., `HWIN-VAR-001.json`)
- `BENCHMARK_STATISTICS.md` (any CI tables)
- `MASTER_BENCHMARK_SUMMARY.csv` (if it contains CIs)
- Any figures/tables containing CIs

**Files that do NOT need regeneration:**
- Model predictions (not stored)
- `all_results.json` structure (only CI values change)
- Protocol (only interpretation changes)

### 9. Does the benchmark protocol need modification?
**YES** — for future versions. The protocol should clarify:
- Whether "5 seeds" requires different GroupKFold partitions (requires custom GroupKFold with shuffling)
- Or whether "5 deterministic repetitions" is the intended design
- Current v1.0: 5 deterministic repetitions of identical folds

### 10. Does the ESSD manuscript need modification?
**YES** — the following must be updated:
- Methods section: clarify that 5 seed repetitions are deterministic (identical folds)
- Results section: report CIs with n=5 (wider by factor ~3)
- Statistical interpretation: note that only 5 unique fold partitions were evaluated
- Uncertainty statements: all CIs are ~3× wider than reported

---

## Evidence Summary

| Evidence | Finding |
|----------|---------|
| Source code (run_full_benchmark_fixed.py) | Outer `seed` variable never used; sampling `random_state=42` fixed; models `random_state=42` fixed; GroupKFold has no `random_state` |
| Fold identity diagnostic (02_FOLD_IDENTITY_ANALYSIS.csv) | All 5 seeds × 5 folds produce identical train/test group hashes |
| Output JSON structure | Only aggregated metrics stored (mean, CI, n_folds=25); no per-fold values |
| CI recovery from aggregated stats | 25 values = 5 unique values × 5 identical repetitions; std recovered; corrected CI computed with n=5 |
| CI comparison (CI_COMPARISON.csv) | All 385 CIs widened by factor 3.0081; means unchanged |
| CI verification | Two independent calculation methods match to < 1e-15 |

---

## Recommended Correction Procedure

1. **Compute corrected CIs** for all 385 metric combinations using n=5, df=4, t=2.776
2. **Update** `GRQA_full_benchmark_complete.json` and 11 per-variable JSONs
3. **Regenerate** `BENCHMARK_STATISTICS.md` and any CI-dependent tables/figures
4. **Update** `MASTER_BENCHMARK_SUMMARY.csv` if it contains CIs
5. **Document** in `LIMITATIONS.md`: "CIs in v1.0 reported with n=25; corrected to n=5 (5 unique folds). Reported CIs are ~3× too narrow."
6. **Update** protocol for v1.1+ to specify whether different folds per seed are required

---

## Verdict: **CI CORRECTION ONLY**

No full benchmark recomputation required. The 1,925 model fits were correctly computed; only the uncertainty quantification (CIs) used the wrong sample size. All point estimates are valid.