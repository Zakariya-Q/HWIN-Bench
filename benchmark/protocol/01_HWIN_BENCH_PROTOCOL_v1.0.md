# HWIN-Bench v1.0 Official Benchmark Protocol

**Status**: FROZEN — Immutable scientific contract
**Version**: 1.0.0
**Date**: 2025-08-06
**Repository**: HWIN_Bench_v1_RELEASE (canonical)
**Author**: Independent Specification Resolution

---

> **This document is the single immutable benchmark protocol for HWIN-Bench v1.0. It is the scientific contract. All benchmark computations, manuscript claims, and repository artifacts MUST conform to this protocol. Any deviation is a protocol violation.**

---

## 1. SCOPE

This protocol defines the **complete, immutable, canonical benchmark** for HWIN-Bench v1.0. It specifies every computational parameter, data source, model, metric, and output format. No parameter may be changed without a new protocol version.

**Scope**: Global River Quality Archive (GRQA) v1.4 regression benchmark on 13 canonical water quality variables using 7 classical ML models with 5×5 GroupKFold cross-validation.

---

## 2. DATASETS

### 2.1 Canonical Datasets (5 Total)

| Dataset ID | Source | Version | License | Canonical Path |
|------------|--------|---------|---------|----------------|
| HWIN-GRQA-V1-4 | Global River Quality Archive | v1.4 | CC-BY-4.0 | `scripts/archive/output_real_hwin_bench_rc1/canonical/HWIN-GRQA-V1-4/` |
| HWIN-WQP-SFBAY | USGS/EPA WQP (San Francisco Bay) | 1.0.0 | CC0-1.0 | `scripts/archive/output_real_hwin_bench_rc1/canonical/HWIN-WQP-SFBAY/` |
| HWIN-STORET-CA | EPA STORET California | 1.0.0 | CC0-1.0 | `scripts/archive/output_real_hwin_bench_rc1/STORET_CA/STORET_CA/` |
| HWIN-STORET-TX | EPA STORET Texas | 1.0.0 | CC0-1.0 | `scripts/archive/output_real_hwin_bench_rc1/STORET_TX/STORET_TX/` |
| HWIN-STORET-RI | EPA STORET Rhode Island | 1.0.0 | CC0-1.0 | `scripts/archive/output_real_hwin_bench_rc1/STORET_RI/STORET_RI/` |

### 2.2 Dataset Integrity

- **Checksums**: SHA256 computed at deposition time (recorded in `dataset.json`)
- **Provenance**: Full chain from raw source → download → extraction → canonicalization → validation → splits → benchmark (documented per dataset)
- **CBS Validation**: All 5 datasets MUST pass CBS validation before benchmark execution

---

## 3. CANONICAL VARIABLE ONTOLOGY (CVO v1.0)

### 3.1 Canonical Source
**File**: `/c/Users/lenovo/knowledge/canonical_variable_ontology.csv` (51 variables, HWIN-VAR-001 through HWIN-VAR-051)

### 3.2 Variable Mappings
**File**: `/c/Users/lenovo/knowledge/variable_synonym_dictionary.csv` (89 mappings)
- Tier 1 (Exact): 52 mappings
- Tier 2 (Synonym): 28 mappings  
- Tier 3 (Expert): 9 mappings

### 3.3 Benchmarkable Variables (GRQA v1.4)

**Inclusion Criterion**: MIN_SAMPLES = 100 observations in canonical GRQA data after harmonization

| Variable ID | Canonical Name | GRQA Observations | Included |
|-------------|----------------|-------------------|----------|
| HWIN-VAR-001 | Water Temperature | 5,508,690 | YES |
| HWIN-VAR-002 | pH | 4,702,926 | YES |
| HWIN-VAR-003 | Dissolved Oxygen | 2,758,590 | YES |
| HWIN-VAR-004 | Turbidity | ≥100 | YES |
| HWIN-VAR-005 | Specific Conductance | ≥100 | YES |
| HWIN-VAR-008 | Nitrate Nitrogen | 2,343,593 | YES |
| HWIN-VAR-009 | Ammonium Nitrogen | 999,283 | YES |
| HWIN-VAR-010 | Phosphate Phosphorus | 2,858,114 | YES |
| HWIN-VAR-014 | DO Percent Saturation | 1,690,075 | YES |
| HWIN-VAR-015 | Total Suspended Solids | 1,308,520 | YES |
| HWIN-VAR-022 | Biochemical Oxygen Demand | ≥100 | YES |
| HWIN-VAR-023 | Chemical Oxygen Demand | 119,220 | YES |
| HWIN-VAR-033 | Nitrite Nitrogen | 1,310,136 | YES |

**Total Benchmarkable Variables**: 13

---

## 4. SAMPLING

### 4.1 MAX_SAMPLES Cap
- **Value**: 200,000 observations per variable
- **Random State**: 42 (fixed)
- **Method**: `var_data.sample(n=200000, random_state=42).reset_index(drop=True)`
- **Applied**: After harmonization, before feature engineering
- **Affected**: 12 of 13 variables (HWIN-VAR-023 COD has 119,220 < 200K)

### 4.2 MIN_SAMPLES Threshold
- **Value**: 100 observations (canonical)
- **Applied**: During variable selection for benchmarking
- **Result**: 13 benchmarkable variables

---

## 5. FEATURE ENGINEERING

**Canonical Function**: `feats()` in `benchmark/run_full_benchmark_fixed.py`

| Feature | Source | Transformation |
|---------|--------|----------------|
| latitude | `latitude` | Direct (float32) |
| longitude | `longitude` | Direct (float32) |
| year | `timestamp` | `dt.dt.year.fillna(2000).astype(int)` |
| month | `timestamp` | `dt.dt.month.fillna(6).astype(int)` |
| day_of_year | `timestamp` | `dt.dt.dayofyear.fillna(180).astype(int)` |
| sin_doy | `day_of_year` | `sin(2π × doy / 365.25)` |
| cos_doy | `day_of_year` | `cos(2π × doy / 365.25)` |

**Output**: 7 features, `float32` array

---

## 6. SPLIT PROTOCOL (Official Split Engine)

### 6.1 Strategy
- **Method**: GroupKFold by `station_id` (string)
- **Grouping Variable**: `station_id` (cast to string)
- **Number of Folds**: 5
- **Number of Repetitions**: 5 seeds

### 6.2 Seeds (Canonical)
**Seeds**: `[42, 123, 256, 512, 1024]` (5 seeds)

### 6.3 Split Procedure
For each seed:
1. Initialize `GroupKFold(n_splits=5)`
2. Generate 5 (train, test) index pairs
3. Store split specification with SHA-256 hash
4. Repeat for all 5 seeds

### 6.4 Total Evaluations
- **Per Model-Variable**: 25 (5 seeds × 5 folds)
- **Total Model Fits**: 13 vars × 7 models × 5 seeds × 5 folds = **2,275**

---

## 7. OFFICIAL MODEL SET (7 Classical Models)

| Model | Class | Hyperparameters | Source |
|-------|-------|-----------------|--------|
| Linear Regression | `LinearRegression` | `{}` | `sklearn.linear_model` |
| Ridge | `Ridge` | `alpha=1.0` | `sklearn.linear_model` |
| Lasso | `Lasso` | `alpha=0.1, max_iter=5000` | `sklearn.linear_model` |
| ElasticNet | `ElasticNet` | `alpha=0.1, l1_ratio=0.5, max_iter=5000` | `sklearn.linear_model` |
| Random Forest | `RandomForestRegressor` | `n_estimators=200, max_depth=None, min_samples_split=2, random_state=42, n_jobs=-1` | `sklearn.ensemble` |
| Extra Trees | `ExtraTreesRegressor` | `n_estimators=200, max_depth=None, min_samples_split=2, random_state=42, n_jobs=-1` | `sklearn.ensemble` |
| Gradient Boosting | `GradientBoostingRegressor` | `n_estimators=200, learning_rate=0.1, max_depth=3, random_state=42` | `sklearn.ensemble` |

**Source**: `src/hwin_bench/hwin_bench/baselines/classical/_sklearn_models.py`

### 7.1 Extended Models (NOT in v1.0)
| Model | Status | Repository |
|-------|--------|------------|
| XGBoost | FUTURE (v1.1) | `hwin-baselines` |
| LightGBM | FUTURE (v1.1) | `hwin-baselines` |
| CatBoost | FUTURE (v1.1) | `hwin-baselines` |
| HWIN-Net (Deep Learning) | EXTERNAL (experimental) | `hwin-net` |

---

## 8. METRICS (5 Regression Metrics)

| Metric | Function | Formula |
|--------|----------|---------|
| MAE | `mean_absolute_error` | `mean(\|y_true - y_pred\|)` |
| RMSE | `root_mean_squared_error` | `sqrt(mean((y_true - y_pred)²))` |
| R² | `r2_score` | `1 - SS_res/SS_tot` (handles SS_tot=0) |
| MAPE | `mean_absolute_percentage_error` | `mean(\|(y_true-y_pred)/y_true\|)*100` (y_true≠0) |
| MedAE | `median_absolute_error` | `median(\|y_true - y_pred\|)` |

**Source**: `src/hwin_bench/hwin_bench/evaluation/metrics.py`

---

## 9. EVALUATION PROTOCOL

### 9.1 Per-Fold Evaluation
For each (variable, model, seed, fold):
1. Extract train/test indices from GroupKFold
2. Instantiate model with fixed hyperparameters
3. Fit on `X_train, y_train`
4. Predict on `X_test`
5. Compute all 5 metrics
6. Store results

### 9.2 Metric Aggregation
For each (variable, model) across 25 folds:
- Mean, Std, Median, Min, Max
- **95% CI**: t-distribution (mean ± t_{0.975, 24} × SEM)
- Count of valid folds (must be 25)

### 9.3 Statistical Testing
- **Kruskal-Wallis**: Across all models per variable
- **Wilcoxon Signed-Rank**: Pairwise model comparisons
- **Cliff's Delta**: Effect size for pairwise
- **Multiple Testing Correction**: **Holm-Bonferroni step-down** (mandatory)
- **Comparisons**: 91 (7 models × 13 variables)

**Source**: `src/hwin_bench/hwin_bench/evaluation/statistics.py` (must implement Holm-Bonferroni)

---

## 10. CONFIDENCE INTERVALS

### 10.1 Method
- **Type**: t-distribution CI for mean
- **Confidence**: 95%
- **Formula**: `mean ± t_{0.975, n-1} × SEM`
- **Applied To**: Mean of 25 fold evaluations per model-variable

**Source**: `src/hwin_bench/hwin_bench/evaluation/confidence_intervals.py` → `mean_confidence_interval()`

---

## 11. OUTPUT FORMATS

### 11.1 Per-Variable JSON (`HWIN-VAR-XXX_results.json`)
```json
{
  "model_name": {
    "metrics": {
      "r2": {"mean": 0.4363, "std": 0.12, "median": 0.42, "ci_95": [0.214, 0.658], "n_folds": 25, "all_values": [...]},
      "mae": {...},
      "rmse": {...},
      "mape": {...},
      "medae": {...}
    },
    "total_time": 569.5,
    "avg_fold_time": 11.4,
    "n_folds_completed": 25
  }
}
```

### 11.2 Aggregated JSON (`all_results.json`)
All variables combined with same structure.

### 11.3 CBS Canonical Data (CSV)
| File | Columns |
|------|---------|
| `observations.csv` | observation_id, dataset_id, station_id, canonical_variable_id, value, unit, timestamp, latitude, longitude, country, ... |
| `stations.csv` | station_id, latitude, longitude, country_code, water_body_type, ... |
| `variables.csv` | canonical_variable_id, canonical_name, canonical_unit, category, ... |
| `dataset.json` | Metadata: ID, title, description, license, DOI, spatial/temporal coverage, checksums |

---

## 12. RANDOM SEED POLICY (Canonical)

| Component | Seeds | Policy |
|-----------|-------|--------|
| Benchmark (GroupKFold) | `[42, 123, 256, 512, 1024]` | 5 seeds × 5 folds |
| Data Sampling | `42` | Fixed for 200K cap |
| Model Training | `42` | Fixed per model (`random_state=42`) |
| hwin-baselines | `[42, 123, 256, 512, 1024]` | External (different repo) |
| hwin-net | `[42, 123, 456, 789, 999]` | External (different repo) |

**Canonical for v1.0**: `[42, 123, 256, 512, 1024]`

---

## 13. CANONICAL EXECUTION COMMAND

```bash
cd /c/Users/lenovo/HWIN_Bench_v1_RELEASE
python benchmark/run_full_benchmark_fixed.py
```

**Expected**: 13 variables × 7 models × 5 seeds × 5 folds = 2,275 model fits
**Runtime**: ~5-6 hours on CPU (n_jobs=-1 for RF/ET/GB)
**Output**: `output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete.json`

---

## 13. CANONICAL BENCHMARK SCRIPT

**File**: `benchmark/run_full_benchmark_fixed.py` (ONLY)
**Archived**: `benchmark/run_full_benchmark.py` → LEGACY (archive)

---

## 14. VALIDATION REQUIREMENTS (Pre-Benchmark)

All 5 datasets MUST pass CBS validation before benchmark execution:
- Completeness (8 rules)
- Range Validity (38 per variable)
- Referential Integrity (3 rules)
- Duplicate Detection (2 rules)
- Temporal Consistency (4 rules)
- Spatial Consistency (3 rules)

**Certification Levels**: Gold / Silver / Bronze / Uncertified

---

## 15. PROVENANCE REQUIREMENTS

All 5 datasets MUST have complete provenance chains:
- Raw source → download (URL, date, SHA256) → extraction → canonicalization (CVO mapping log, unit conversion log) → CBS validation → split generation → benchmark execution
- Per-observation provenance in CBS: source_dataset, source_variable, transformation_applied, conversion_factor, quality_flag_original

---

## 16. TRANSFER LEARNING (Canonical)

**Protocol**: Train on GRQA subset matched to STORET region → evaluate on STORET target
**Shared Variables**: 7-10 per dataset pair
**Metric**: R² on target domain
**Status**: Must fix NaN bug before benchmark execution

---

## 17. FIGURES & TABLES (Canonical Sources)

| Figure | Type | Source Data |
|--------|------|-------------|
| Fig 1: Pipeline Architecture | Diagram | `knowledge/pipeline_architecture.md` |
| Fig 2: Global Coverage | Map | `output/global/global_geographic_coverage.csv` |
| Fig 3: Variable Heatmap | Heatmap | `output/dataset_variable_inventory.csv` |
| Fig 4: Temporal Coverage | Timeline | `output/global/global_temporal_coverage.csv` |
| Fig 5: Benchmark Comparison | Bar | `output/benchmark_summary.md` |
| Fig 6: Transfer Matrix | Heatmap | `output/transfer_heatmap.png` |
| Fig 7: Missing Data Robustness | Line | `output/grqa_observation_accounting.csv` |
| Fig 8: FAIR Radar | Radar | `output/FAIR_report.md` |

| Table | Source |
|-------|--------|
| Table 1: Integrated Datasets | `output/global/global_dataset_inventory.csv` |
| Table 2: Canonical Variables | `output/global/global_variable_inventory.csv` |
| Table 3: Metadata Completeness | `output/global/global_metadata_summary.csv` |
| Table 4: Benchmark Tasks | `knowledge/benchmark_task_framework.md` |
| Table 5: GRQA Results | `output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete.json` |
| Table 6: STORET Results | `output/benchmark_summary.md` (needs traceability) |
| Table 7: Transfer Results | `output/transfer_matrix_raw.csv` |
| Table 8: FAIR Assessment | `output/FAIR_report.md` (qualitative only) |
| Table 9: Compute Requirements | `output/memory_pipeline_audit.md` |

---

## 18. PROTOCOL COMPLIANCE

**Every benchmark run, manuscript claim, and repository artifact MUST conform to this protocol.**

**Violations include**:
- Using any script other than `benchmark/run_full_benchmark_fixed.py`
- Changing MIN_SAMPLES from 100
- Using seeds other than `[42, 123, 256, 512, 1024]`
- Using models other than the 7 official
- Using split method other than GroupKFold by station_id
- Omitting Holm-Bonferroni correction
- Reporting FAIR numeric score (use qualitative A-/A only)
- Reporting transfer learning direction incorrectly

---

**END OF PROTOCOL**

*This document is frozen. Any changes require a new protocol version (v1.1, v1.2, etc.) with full re-certification.*