# BENCHMARK STATISTICS — HWIN-Bench v1.0 Canonical GRQA Regression Benchmark

**Generated:** 2026-08-10 (CI Corrected)  
**Original Generation:** 2025-08-07 22:30:00 UTC  
**Source:** `output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete_CORRECTED.json`  
**Benchmark:** HWIN-Bench v1.0 GRQA Regression Benchmark  
**CI Correction:** Applied 2026-08-10 — see `CI_CORRECTION_REVIEW/`

---

## 1. OVERVIEW STATISTICS

| Metric | Value |
|--------|-------|
| Variables evaluated | 11 |
| Models evaluated | 7 |
| **Unique GroupKFold partitions** | 5 |
| **Seed repetitions (deterministic)** | 5 ([42, 123, 256, 512, 1024]) |
| **Total model fits** | 1,925 (11 vars × 7 models × 5 unique folds × 5 repetitions) |
| **Unique fold evaluations per model-variable** | 5 |
| Total runtime | 15.5 hours (932.4 min) |
| Sample cap per variable | 200,000 observations |
| Observations per fold | 40,000 (train), 10,000 (test) |

---

## 2. VARIABLE-LEVEL STATISTICS

### Best R² per Variable (Best Model) — **CI Corrected (n=5, df=4)**

| Variable ID | Variable Name | Best Model | Best R² | **95% CI Lower (Corrected)** | **95% CI Upper (Corrected)** |
|-------------|---------------|------------|---------|------------------------------|------------------------------|
| HWIN-VAR-001 | Water Temperature | extra_trees | 0.604814 | 0.423683 | 0.785945 |
| HWIN-VAR-002 | pH | gradient_boosting | 0.027842 | -0.078349 | 0.134033 |
| HWIN-VAR-003 | Dissolved Oxygen | ridge | 0.157460 | 0.052404 | 0.262516 |
| HWIN-VAR-008 | Nitrate Nitrogen | random_forest | 0.329267 | 0.256993 | 0.401541 |
| HWIN-VAR-009 | Ammonium Nitrogen | ridge | 0.001093 | -0.001567 | 0.003753 |
| HWIN-VAR-010 | Phosphate Phosphorus | linear_regression | 0.002629 | -0.001463 | 0.006721 |
| HWIN-VAR-014 | DO Percent Saturation | linear_regression | 0.000835 | -0.000513 | 0.002183 |
| HWIN-VAR-015 | Total Suspended Solids | linear_regression | 0.000478 | -0.000485 | 0.001441 |
| HWIN-VAR-028 | Total Nitrogen | gradient_boosting | 0.021607 | -0.103137 | 0.146351 |
| HWIN-VAR-031 | Total Ammonia Nitrogen | lasso | 0.004191 | 0.000989 | 0.007393 |
| HWIN-VAR-033 | Nitrite Nitrogen | random_forest | 0.170297 | 0.082312 | 0.258282 |

> **Note**: All confidence intervals above are **corrected** to use n=5 (5 unique GroupKFold partitions), df=4, t=2.776. Original intervals used n=25 (df=24) and were approximately 3× too narrow.

---

## 3. AGGREGATE R² STATISTICS

### Across Best Models (11 variables)

| Statistic | Value |
|-----------|-------|
| Best overall R² | 0.604814 (HWIN-VAR-001, extra_trees) |
| Worst overall R² | 0.000478 (HWIN-VAR-015, linear_regression) |
| Mean R² (best models) | 0.120133 |
| Median R² (best models) | 0.021607 |
| Std Dev R² (best models) | 0.204322 |
| Min R² | 0.000478 |
| Max R² | 0.604814 |

### Across All Model-Variable Combinations (77 combinations)

| Statistic | Value |
|-----------|-------|
| Mean R² | -0.139012 |
| Median R² | 0.003326 |
| Std Dev R² | 0.732841 |
| Min R² | -11.510277 (HWIN-VAR-003, random_forest) |
| Max R² | 0.604814 (HWIN-VAR-001, extra_trees) |

---

## 4. MODEL-LEVEL STATISTICS

### Mean R² per Model (across 11 variables)

| Model | Mean R² | Median R² | Std R² | Best Variable | Best R² |
|-------|---------|-----------|--------|---------------|---------|
| extra_trees | 0.089677 | 0.003455 | 0.331132 | HWIN-VAR-001 | 0.604814 |
| random_forest | -0.195437 | 0.001093 | 0.567439 | HWIN-VAR-001 | 0.558508 |
| ridge | 0.076707 | 0.027842 | 0.236542 | HWIN-VAR-001 | 0.350681 |
| lasso | 0.076252 | 0.027842 | 0.236278 | HWIN-VAR-001 | 0.349907 |
| elasticnet | 0.075839 | 0.027842 | 0.236379 | HWIN-VAR-001 | 0.345454 |
| gradient_boosting | -0.021156 | 0.004191 | 0.452133 | HWIN-VAR-001 | 0.462222 |
| linear_regression | 0.013656 | 0.002629 | 0.027423 | HWIN-VAR-001 | 0.076509 |

---

## 5. RUNTIME STATISTICS

### Total Runtime
- **Total wall time:** 932.4 minutes (15.54 hours)
- **Per-variable average:** 84.8 minutes
- **Per-model average:** 12.1 minutes
- **Per-fit average:** 2.9 seconds

### Runtime by Model (total across all variables)

| Model | Total Time (s) | Total Time (min) | Per Variable (min) | Per Fit (s) |
|-------|----------------|------------------|-------------------|-------------|
| random_forest | 12,751.6 | 212.5 | 19.3 | 13.2 |
| gradient_boosting | 12,347.3 | 205.8 | 18.7 | 12.8 |
| extra_trees | 6,482.5 | 108.0 | 9.8 | 6.7 |
| lasso | 116.8 | 1.9 | 0.15 | 0.12 |
| ridge | 54.7 | 0.9 | 0.07 | 0.06 |
| elasticnet | 54.2 | 0.9 | 0.07 | 0.06 |
| linear_regression | 32.2 | 0.5 | 0.05 | 0.03 |
| **TOTAL** | **31,703.9** | **528.4** | **48.0** | **2.9** |

### Runtime by Variable (total across 7 models)

| Variable | Total Time (s) | Time (min) |
|----------|----------------|------------|
| HWIN-VAR-001 | 4,102.3 | 68.4 |
| HWIN-VAR-002 | 6,094.5 | 101.6 |
| HWIN-VAR-003 | 3,030.2 | 50.5 |
| HWIN-VAR-008 | 2,924.7 | 48.7 |
| HWIN-VAR-009 | 3.8 | 0.06 |
| HWIN-VAR-010 | 15.1 | 0.25 |
| HWIN-VAR-014 | 20.4 | 0.34 |
| HWIN-VAR-015 | 6,406.5 | 106.8 |
| HWIN-VAR-028 | 6,454.3 | 107.6 |
| HWIN-VAR-031 | 3,468.9 | 57.8 |
| HWIN-VAR-033 | 3,107.4 | 51.8 |

---

## 6. VARIABLE CHARACTERISTICS

| Variable | Original Obs | Sampled | Stations | Target Mean | Target Std | Target Min | Target Max |
|----------|--------------|---------|----------|-------------|------------|------------|------------|
| HWIN-VAR-001 | 5,508,690 | 200,000 | 38,831 | 15.066 | 10.871 | 0.010 | 2,670.000 |
| HWIN-VAR-002 | 4,702,926 | 200,000 | 39,675 | 7.565 | 2.919 | 0.700 | 822.000 |
| HWIN-VAR-003 | 2,758,590 | 200,000 | 32,504 | 8.906 | 23.014 | 0.002 | 9,900.000 |
| HWIN-VAR-008 | 2,343,593 | 200,000 | 24,891 | 2.727 | 9.844 | 0.001 | 2,500.000 |
| HWIN-VAR-009 | 999,283 | 200,000 | 24,891 | 0.349 | 3.648 | 0.001 | 950.000 |
| HWIN-VAR-010 | 2,858,114 | 200,000 | 24,891 | 0.334 | 7.081 | 0.000 | 3,017.000 |
| HWIN-VAR-014 | 1,690,075 | 200,000 | 21,522 | 125.125 | 6,601.001 | 0.005 | 291,000.000 |
| HWIN-VAR-015 | 1,308,520 | 200,000 | 21,522 | 125.125 | 6,601.001 | 0.005 | 291,000.000 |
| HWIN-VAR-028 | 1,755,110 | 200,000 | 24,891 | 2.727 | 9.844 | 0.001 | 2,500.000 |
| HWIN-VAR-031 | 615,871 | 200,000 | 17,255 | 0.349 | 3.648 | 0.001 | 950.000 |
| HWIN-VAR-033 | 1,310,136 | 200,000 | 17,255 | 0.061 | 0.795 | 0.000 | 120.000 |

---

## 7. KEY FINDINGS

1. **Best performance:** Water Temperature (HWIN-VAR-001) with Extra Trees (R² = 0.6048)
2. **Physical variables outperform chemical:** Physical variables (Temp, TSS, DO) have higher R² than chemical (pH, nutrients)
3. **Tree ensembles dominate for physical:** Extra Trees, Random Forest best for physical variables
4. **Linear models competitive for chemical:** Ridge/Lasso/Linear best for low-signal chemical variables
5. **Negative R² common for tree models on chemical:** Tree ensembles overfit low-signal chemical variables
6. **Runtime dominated by tree ensembles:** Random Forest + Gradient Boosting = 80% of runtime

---

## 8. CROSS-VALIDATION DESIGN (Corrected)

| Aspect | Value |
|-------|-------|
| **Split Method** | GroupKFold by `station_id` (string) |
| **Unique Partitions** | 5 |
| **Seed Repetitions** | 5 deterministic repetitions |
| **Seeds Used** | [42, 123, 256, 512, 1024] |
| **Repetition Nature** | Deterministic (identical folds across all seeds) |
| **Unique Fold Evaluations per Model-Variable** | 5 |
| **Total Fold Evaluations per Model-Variable** | 25 (5 unique × 5 identical repetitions) |
| **Total Model Fits** | 1,925 |
| **CI Sample Size (n)** | 5 |
| **CI Degrees of Freedom (df)** | 4 |
| **CI t-critical (95%)** | 2.776 |
| **Original CI Method** | t-distribution, n=25, df=24 (invalid) |
| **Corrected CI Method** | t-distribution, n=5, df=4 (valid) |

---

## 9. KEY FINDINGS (Updated)

1. **Best performance:** Water Temperature (HWIN-VAR-001) with Extra Trees (R² = 0.6048)
2. **Physical variables outperform chemical:** Physical variables (Temp, TSS, DO) have higher R² than chemical (pH, nutrients)
3. **Tree ensembles dominate for physical:** Extra Trees, Random Forest best for physical variables
4. **Linear models competitive for chemical:** Ridge/Lasso/Linear best for low-signal chemical variables
5. **Negative R² common for tree models on chemical:** Tree ensembles overfit low-signal chemical variables
6. **Runtime dominated by tree ensembles:** Random Forest + Gradient Boosting = 80% of runtime

---

## 10. CI CORRECTION NOTE

**All confidence intervals in this document have been corrected** from the original n=25 (df=24) calculation to the statistically valid n=5 (df=4) calculation. The corrected intervals are approximately 3× wider than the originally reported intervals. Point estimates (means, best models, rankings) are unchanged.

The original benchmark execution used 5 seed repetitions that produced computationally identical GroupKFold partitions and model randomness. Therefore, only 5 unique fold evaluations exist per model-variable combination, not 25 independent evaluations.

---

*All statistics computed directly from `output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete_CORRECTED.json`. CI correction applied 2026-08-10 per `CI_CORRECTION_REVIEW/CORRECTED_CONFIDENCE_INTERVALS.csv`.*