# BENCHMARK STATISTICS — HWIN-Bench v1.0 Canonical GRQA Regression Benchmark

**Generated:** 2026-10-08 (canonicalized to Run B + recomputed CIs)
**Canonical run:** `benchmark/results/grqa_recomputation/` (2026-08-06/07 execution; full per-fold values stored)
**Benchmark:** HWIN-Bench v1.0 GRQA Regression Benchmark
**CI method:** n=5 unique GroupKFold partitions, df=4, t=2.776 — computed directly from the canonical run's stored fold values

> **Provenance note (2026-10-08).** This repository previously shipped a
> different execution (`grqa_full_final_groupkfold`, 2026-07-08/09, aggregated
> means only) alongside documents quoting the `grqa_recomputation` run. Per
> benchmark-author decision, `grqa_recomputation` is the **canonical v1.0 run**.
> Its 25 recorded fold evaluations per model-variable are 5 deterministic
> repetitions of the same 5-fold partition set (verified: identical repetition
> blocks in all but 3 of 77 combinations, where negligible float noise exists).
> All statistics below are recomputed directly from those stored fold values.
> CI values in this file supersede any earlier CI figures appearing in
> historical certificates or audit documents.

---

## 1. OVERVIEW STATISTICS

| Metric | Value |
|--------|-------|
| Variables evaluated | 11 |
| Models evaluated | 7 |
| **Unique GroupKFold partitions** | 5 |
| **Seed repetitions (deterministic)** | 5 ([42, 123, 256, 512, 1024]) |
| **Total model fits** | 1,925 (11 vars × 7 models × 5 unique folds × 5 repetitions) |
| **Unique fold evaluations per model-variable** | 5 (25 recorded = 5 unique × 5 identical repetitions) |
| Total runtime | ~15.5 hours wall-clock (canonical certified execution) |
| Sample cap per variable | 200,000 observations |

---

## 2. VARIABLE-LEVEL STATISTICS

### Best R² per Variable (Best Model) — **n=5, df=4, t=2.776**

| Variable ID | Variable Name | Best Model | Best R² | **95% CI Lower** | **95% CI Upper** |
|-------------|---------------|------------|---------|------------------|------------------|
| HWIN-VAR-001 | Water Temperature | extra_trees | 0.604814 | 0.252502 | 0.957125 |
| HWIN-VAR-002 | pH | gradient_boosting | 0.027842 | -0.118362 | 0.174046 |
| HWIN-VAR-003 | Dissolved Oxygen | ridge | 0.157460 | -0.002591 | 0.317512 |
| HWIN-VAR-008 | Nitrate Nitrogen | random_forest | 0.329267 | 0.225065 | 0.433469 |
| HWIN-VAR-009 | Ammonium Nitrogen | ridge | 0.001093 | -0.000552 | 0.002738 |
| HWIN-VAR-010 | Phosphate Phosphorus | linear_regression | 0.002629 | -0.000905 | 0.006163 |
| HWIN-VAR-014 | DO Percent Saturation | linear_regression | 0.000835 | -0.000702 | 0.002372 |
| HWIN-VAR-015 | Total Suspended Solids | linear_regression | 0.000478 | -0.000660 | 0.001616 |
| HWIN-VAR-028 | Total Nitrogen | gradient_boosting | 0.021607 | -0.187768 | 0.230982 |
| HWIN-VAR-031 | Total Ammonia Nitrogen | lasso | 0.004191 | 0.000209 | 0.008173 |
| HWIN-VAR-033 | Nitrite Nitrogen | random_forest | 0.170297 | 0.036179 | 0.304415 |

> **Note**: All confidence intervals are computed on the 5 unique GroupKFold
> fold values (n=5, df=4, t=2.776). The 25 recorded evaluations contain these
> 5 values repeated identically; treating them as 25 independent observations
> would understate the interval width by ≈3×.

### Aggregate (best models, 11 variables)

| Statistic | Value |
|-----------|-------|
| Best overall R² | 0.604814 (HWIN-VAR-001, extra_trees) |
| Worst overall R² | 0.000478 (HWIN-VAR-015, linear_regression) |
| Mean R² (best models) | 0.120047 |
| Median R² (best models) | 0.021607 |

---

## 3. CROSS-VALIDATION DESIGN

| Aspect | Value |
|-------|-------|
| **Split Method** | GroupKFold by `station_id` (string) |
| **Unique Partitions** | 5 |
| **Seed Repetitions** | 5 deterministic repetitions |
| **Seeds Used** | [42, 123, 256, 512, 1024] |
| **Repetition Nature** | Deterministic — seed value not consumed by any stochastic operation |
| **Total Fold Evaluations per Model-Variable** | 25 (5 unique × 5 identical repetitions) |
| **Total Model Fits** | 1,925 |
| **CI Sample Size (n)** | 5 |
| **CI Degrees of Freedom (df)** | 4 |
| **CI t-critical (95%)** | 2.776 |

---

## 4. KEY FINDINGS

1. **Best performance:** Water Temperature (HWIN-VAR-001) with Extra Trees (R² = 0.6048)
2. **Physical variables outperform chemical:** temperature/DO transfer better than nutrients
3. **Tree ensembles dominate for physical variables:** Extra Trees / Random Forest
4. **Linear models competitive for low-signal chemical variables**
5. **Runtime dominated by tree ensembles**

---

*Statistics computed directly from `benchmark/results/grqa_recomputation/all_results.json` (canonical run, per-fold values stored). CIs recomputed 2026-10-08 from the 5 unique fold values per model-variable.*
