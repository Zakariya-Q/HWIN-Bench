# DATA_DICTIONARY.md — HWIN-Bench v1.0

Complete reference for variables, columns, and data structures in HWIN-Bench v1.0.

---

## Canonical Benchmark Schema (CBS)

Every harmonized dataset follows the same CBS structure:

### Observations (`observations.csv`)

```csv
observation_id,dataset_id,station_id,canonical_variable_id,value,unit,timestamp,latitude,longitude,country,site_name,param_name,source,quality_flag,percentile,original_value,original_unit,country_iso
```

| Column | Type | Description |
|--------|------|-------------|
| observation_id | UUID | Unique per observation (generated during canonicalization) |
| dataset_id | String | HWIN dataset identifier (e.g., HWIN-GRQA-V1-4) |
| station_id | String | Original station identifier |
| canonical_variable_id | String | CVO variable ID (HWIN-VAR-XXX) |
| value | Float | Harmonized value in SI/canonical units |
| unit | String | Canonical unit (e.g., K, mg/L, pH unit) |
| timestamp | ISO 8601 | UTC timestamp |
| latitude | Float | WGS84 decimal degrees |
| longitude | Float | WGS84 decimal degrees |
| country | String | ISO 3166-1 alpha-2 country code |
| site_name | String | Original station name |
| param_name | String | Original parameter name from source |
| source | String | Source dataset (GEMSTAT, WQP, GRQA_v1.4, etc.) |
| quality_flag | Integer | Original quality flag (0=good, >0=various issues) |
| percentile | Float | Optional: percentile rank within station-variable |
| original_value | Float | Value before unit conversion |
| original_unit | String | Unit before conversion |
| country_iso | String | ISO 3166-1 alpha-2 (duplicate of country for convenience) |

---

### Stations (`stations.json`)

```json
[
  {
    "station_id": "ARG00003",
    "station_name": "Paraguay River - at Puerto Bermejo",
    "latitude": -26.925888,
    "longitude": -58.507027,
    "station_type": "river",
    "country_code": "AR"
  }
]
```

| Field | Type | Description |
|-------|------|-------------|
| station_id | String | Original station identifier |
| station_name | String | Original station name |
| latitude | Float | WGS84 decimal degrees |
| longitude | Float | WGS84 decimal degrees |
| station_type | String | river, lake, estuary, groundwater, etc. |
| country_code | String | ISO 3166-1 alpha-2 |

---

### Variables (`variables.csv`)

```csv
canonical_variable_id,canonical_name,definition,si_unit,preferred_datatype,expected_range
HWIN-VAR-001,Water Temperature,The intensity of heat present in water,K,Float,-2 to 40 deg C
```

| Column | Type | Description |
|--------|------|-------------|
| canonical_variable_id | String | CVO variable ID (HWIN-VAR-XXX) |
| canonical_name | String | Human-readable name |
| definition | String | Scientific definition |
| si_unit | String | SI unit |
| preferred_datatype | String | Expected data type (Float, Integer) |
| expected_range | String | Expected physical range |

---

### Dataset Metadata (`dataset.json`)

```json
{
  "dataset_id": "HWIN-GRQA-V1-4",
  "version": "1.4.0",
  "title": "Global River Water Quality Archive (GRQA) v1.4 - HWIN-Bench Harmonized Version",
  "license": "CC-BY-4.0",
  "license_uri": "https://creativecommons.org/licenses/by/4.0/",
  "spatial_coverage": {"type": "global", "countries": 69, "stations": 107000},
  "temporal_coverage": {"start": "1894-01-01", "end": "2023-12-31"},
  "variables": 11,
  "observations": {"canonical_total": 25800000, "benchmarked_max_per_variable": 200000, "benchmarked_total": 2519220},
  "checksums": {"observations.csv": "sha256:...", "stations.json": "sha256:...", "variables.csv": "sha256:..."}
}
```

---

## Ontology Reference

### Canonical Variable Ontology (CVO)
**File**: `ontology/canonical_variable_ontology.csv`  
49 variables (HWIN-VAR-001 to HWIN-VAR-049) with definitions, accepted synonyms, typical units, SI units, expected ranges, measurement methods.

### Variable Synonym Dictionary
**File**: `ontology/variable_synonym_dictionary.csv`  
89 mappings from source variable names to canonical IDs:
- Tier 1 (Exact): 52 mappings
- Tier 2 (Synonym): 28 mappings  
- Tier 3 (Expert): 9 mappings

Sources: GEMS_Water, WQP_2023, NEON_AQUATIC, GLORIA, QUADICA, GRQA_v1.4, STORET, WQP

### Unit Harmonization Rules
**File**: `ontology/unit_harmonization_rules.csv`  
92 conversion rules from source units to SI/canonical units with conversion factors and offsets.

Example:
```
HWIN-VAR-001,K,°C,1,273.15,Kelvin = Celsius + 273.15
HWIN-VAR-003,mol/m³,mg/L,0.03125,0.0,For O2: 1 mg/L = 0.03125 mol/m³
HWIN-VAR-005,S/m,µS/cm,0.0001,0.0,1 µS/cm = 0.0001 S/m
```

---

## Benchmark Variables (11 Canonical)

| Variable ID | Canonical Name | GRQA Observations | SI Unit |
|-------------|----------------|-------------------|---------|
| HWIN-VAR-001 | Water Temperature | 5,508,690 | K |
| HWIN-VAR-002 | pH | 4,702,926 | pH unit |
| HWIN-VAR-003 | Dissolved Oxygen | 2,758,590 | mol/m³ |
| HWIN-VAR-008 | Nitrate Nitrogen | 2,343,593 | mol/m³ |
| HWIN-VAR-009 | Ammonium Nitrogen | 999,283 | mol/m³ |
| HWIN-VAR-010 | Phosphate Phosphorus | 2,858,114 | mol/m³ |
| HWIN-VAR-014 | DO Percent Saturation | 1,690,075 | dimensionless |
| HWIN-VAR-015 | Total Suspended Solids | 1,308,520 | g/m³ |
| HWIN-VAR-028 | Total Nitrogen | 1,755,110 | mol/m³ |
| HWIN-VAR-031 | Total Ammonia Nitrogen | 615,871 | mol/m³ |
| HWIN-VAR-033 | Nitrite Nitrogen | 1,310,136 | mol/m³ |

---

## Benchmark Features (7)

| Feature | Source | Transformation |
|---------|--------|----------------|
| latitude | `latitude` | Direct (float32) |
| longitude | `longitude` | Direct (float32) |
| year | `timestamp` | `dt.dt.year.fillna(2000).astype(int)` |
| month | `timestamp` | `dt.dt.month.fillna(6).astype(int)` |
| day_of_year | `timestamp` | `dt.dt.dayofyear.fillna(180).astype(int)` |
| sin_doy | `day_of_year` | `sin(2π × doy / 365.25)` |
| cos_doy | `day_of_year` | `cos(2π × doy / 365.25)` |

---

## Benchmark Models (7)

| Model | Class | Hyperparameters |
|-------|-------|-----------------|
| Linear Regression | `LinearRegression` | `{}` |
| Ridge | `Ridge` | `alpha=1.0` |
| Lasso | `Lasso` | `alpha=0.1, max_iter=5000` |
| ElasticNet | `ElasticNet` | `alpha=0.1, l1_ratio=0.5, max_iter=5000` |
| Random Forest | `RandomForestRegressor` | `n_estimators=200, max_depth=None, min_samples_split=2, random_state=42, n_jobs=-1` |
| Extra Trees | `ExtraTreesRegressor` | `n_estimators=200, max_depth=None, min_samples_split=2, random_state=42, n_jobs=-1` |
| Gradient Boosting | `GradientBoostingRegressor` | `n_estimators=200, learning_rate=0.1, max_depth=3, random_state=42` |

---

## Metrics (5 Regression Metrics)

| Metric | Function | Formula |
|--------|----------|---------|
| MAE | `mean_absolute_error` | `mean(\|y_true - y_pred\|)` |
| RMSE | `root_mean_squared_error` | `sqrt(mean((y_true - y_pred)²))` |
| R² | `r2_score` | `1 - SS_res/SS_tot` (handles SS_tot=0) |
| MAPE | `mean_absolute_percentage_error` | `mean(\|(y_true-y_pred)/y_true\|)*100` (y_true≠0) |
| MedAE | `median_absolute_error` | `median(\|y_true - y_pred\|)` |

---

## Cross-Validation Design

| Aspect | Value |
|--------|-------|
| Split Method | GroupKFold by `station_id` (string) |
| Unique Partitions | 5 |
| Seed Repetitions | 5 deterministic repetitions |
| Seeds Used | [42, 123, 256, 512, 1024] |
| Repetition Nature | Deterministic (identical folds across all seeds) |
| Unique Fold Evaluations per Model-Variable | 5 |
| Total Fold Evaluations per Model-Variable | 25 (5 unique × 5 identical repetitions) |
| Total Model Fits | 1,925 |
| CI Sample Size (n) | 5 |
| CI Degrees of Freedom (df) | 4 |
| CI t-critical (95%) | 2.776 |

---

## Confidence Intervals

- **Method**: t-distribution CI for mean
- **Confidence**: 95%
- **Formula**: `mean ± t_{0.975, n-1} × SEM`
- **Applied To**: Mean of 5 unique fold evaluations per model-variable
- **Correction**: Changed from original n=25 (df=24) to n=5 (df=4)
- **Width Ratio**: Corrected CIs are ~3.008× wider than originally reported

---

## Statistical Testing (v1.1+)

The following statistical tests are specified in the protocol but **NOT implemented in v1.0**:

| Test | Purpose | Status |
|------|---------|--------|
| Kruskal-Wallis | Across all models per variable | NOT IMPLEMENTED (v1.1+) |
| Wilcoxon Signed-Rank | Pairwise model comparisons | NOT IMPLEMENTED (v1.1+) |
| Cliff's Delta | Effect size for pairwise | NOT IMPLEMENTED (v1.1+) |
| Holm-Bonferroni | Multiple testing correction | NOT IMPLEMENTED (v1.1+) |

Reserved for v1.1+ implementation.

---

## Evaluation Metrics (Implemented)

| Metric | Function | Formula |
|--------|----------|---------|
| MAE | `mean_absolute_error` | `mean(|y_true - y_pred|)` |
| RMSE | `root_mean_squared_error` | `sqrt(mean((y_true - y_pred)²))` |
| R² | `r2_score` | `1 - SS_res/SS_tot` (handles SS_tot=0) |
| MAPE | `mean_absolute_percentage_error` | `mean(|(y_true-y_pred)/y_true|)*100` (y_true≠0) |
| MedAE | `median_absolute_error` | `median(|y_true - y_pred|)` |

---

## CBS Validation (58 Rules)

| Category | Rules | Description |
|--------|-------|-------------|
| Completeness | 8 | Required columns, non-null checks |
| Range Validity | 38 | Physical ranges per variable |
| Referential Integrity | 3 | Station IDs, variable IDs, dataset IDs |
| Duplicate Detection | 2 | Observation IDs, station-variable-timestamp |
| Temporal Consistency | 4 | Timestamp ordering, gaps |
| Spatial Consistency | 3 | Coordinate bounds, station locations |

---

## File Formats

| File | Format | Description |
|------|--------|-------------|
| `observations.csv` | CSV | Canonical observations |
| `stations.json` | JSON | Station metadata |
| `variables.csv` | CSV | Variable metadata |
| `dataset.json` | JSON | Dataset-level metadata |
| `observations.csv` (LFS) | CSV | Large observation files |
| `stations.json` (LFS) | JSON | Large station files |
| `.tex` | LaTeX | Publication tables |
| `.png/.pdf/.svg` | Image | Publication figures |
| `.json` | JSON | Benchmark outputs, metadata |
| `.csv` | CSV | Inventory, manifests, audit logs |
| `.yml` | YAML | Configuration, environment |