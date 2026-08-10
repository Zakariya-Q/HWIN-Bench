# Data Dictionary — HWIN-Bench v1.0

Complete reference for all columns, variables, and codes in HWIN-Bench datasets.

## Canonical Benchmark Schema (CBS) — Observations

### `observations.csv` Columns

| Column | Type | Required | Description | Example |
|--------|------|----------|-------------|---------|
| `observation_id` | UUID | Yes | Unique identifier generated during canonicalization | `1ea03179-93a2-5180-9a27-deeb1f1bfc18` |
| `dataset_id` | String | Yes | HWIN dataset identifier | `HWIN-GRQA-V1-4` |
| `station_id` | String | Yes | Original station identifier from source | `ARG00003` |
| `canonical_variable_id` | String | Yes | CVO variable ID (HWIN-VAR-XXX) | `HWIN-VAR-001` |
| `value` | Float | Yes | Harmonized value in canonical units | `17.6` |
| `unit` | String | Yes | Canonical unit | `K` |
| `timestamp` | ISO 8601 | Yes | UTC timestamp | `2018-08-22T10:45:00Z` |
| `latitude` | Float | Yes | WGS84 decimal degrees | `-26.925888` |
| `longitude` | Float | Yes | WGS84 decimal degrees | `-58.507027` |
| `country` | String | Yes | ISO 3166-1 alpha-2 | `AR` |
| `site_name` | String | No | Original station name | `Paraguay River - at Puerto Bermejo` |
| `param_name` | String | No | Original parameter name from source | `Water Temperature` |
| `source` | String | No | Source dataset within provider | `GEMSTAT` |
| `quality_flag` | Integer | No | Original quality flag (0=good) | `0` |
| `percentile` | Float | No | Percentile rank within station-variable | `45.2` |
| `original_value` | Float | Yes | Value before unit conversion | `17.6` |
| `original_unit` | String | Yes | Unit before conversion | `Deg C` |
| `country_iso` | String | Yes | ISO 3166-1 alpha-2 (mirror of country) | `AR` |

## Stations Metadata

### `stations.json` Fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `station_id` | String | Yes | Unique station identifier | `ARG00003` |
| `station_name` | String | Yes | Human-readable station name | `Paraguay River - at Puerto Bermejo` |
| `latitude` | Float | Yes | WGS84 decimal degrees | `-26.925888` |
| `longitude` | Float | Yes | WGS84 decimal degrees | `-58.507027` |
| `station_type` | String | No | Water body type | `river` |
| `country_code` | String | Yes | ISO 3166-1 alpha-2 | `AR` |

## Variables Metadata

### `variables.csv` Columns

| Column | Type | Required | Description | Example |
|--------|------|----------|-------------|---------|
| `canonical_variable_id` | String | Yes | CVO identifier | `HWIN-VAR-001` |
| `canonical_name` | String | Yes | Human-readable name | `Water Temperature` |
| `definition` | String | Yes | Scientific definition | `The intensity of heat present in water` |
| `si_unit` | String | Yes | SI/canonical unit | `K` |
| `preferred_datatype` | String | Yes | Recommended data type | `Float` |
| `expected_range` | String | No | Typical environmental range | `-2 to 40 deg C (liquid water range)` |

### `accepted_units` (in CVO)
List of source units that map to this canonical variable, pipe-separated: `K|deg C|deg F|deg c`

## Dataset Metadata

### `dataset.json` Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `dataset_id` | String | Yes | HWIN dataset identifier |
| `version` | String | Yes | Dataset version |
| `title` | String | Yes | Full title |
| `description` | String | Yes | Description |
| `license` | String | Yes | License identifier |
| `license_uri` | String | Yes | License URL |
| `cv_mapping_id` | String | Yes | CVO version used |
| `metadata_standard` | String | Yes | Metadata standard (ISO 19115-3) |
| `creators` | Array | Yes | Creator information |
| `publication_year` | Integer | Yes | Year of publication |
| `publisher` | String | Yes | Publisher (Zenodo) |
| `funding` | Array | No | Funding information |
| `related_identifiers` | Array | Yes | Source dataset DOIs/URLs |
| `spatial_coverage` | Object | Yes | Spatial extent |
| `temporal_coverage` | Object | Yes | Temporal extent |
| `variables` | Integer | Yes | Number of canonical variables |
| `observations` | Object | Yes | Observation counts |
| `checksums` | Object | Yes | SHA256 checksums |
| `version_history` | Array | Yes | Version changelog |
| `doi` | String | Yes | Zenodo DOI |
| `is_published` | Boolean | Yes | Publication status |

## Canonical Variable Ontology (CVO)

### `canonical_variable_ontology.csv` Columns

| Column | Description |
|--------|-------------|
| `Canonical_ID` | HWIN-VAR-XXX identifier |
| `Canonical_Name` | Human-readable name |
| `Definition` | Scientific definition |
| `Scientific_Meaning` | Detailed scientific meaning |
| `Accepted_Synonyms` | Comma-separated synonyms |
| `Typical_Units` | Typical units in source data |
| `SI_Unit` | SI unit |
| `Preferred_Datatype` | Recommended data type |
| `Expected_Range` | Expected environmental range |
| `Measurement_Methods` | Common measurement methods |
| `Common_Instruments` | Common instruments |
| `Related_Variables` | Related canonical variables |
| `Parent_Category` | Category (Physical, Chemical, Biological, Hydrological, Meteorological) |
| `accepted_units` | Pipe-separated list of accepted source units |

## Variable Synonym Dictionary

### `variable_synonym_dictionary.csv` Columns

| Column | Description |
|--------|-------------|
| `Synonym` | Source variable name |
| `Canonical_ID` | Target CVO ID |
| `Canonical_Name` | Target CVO name |
| `Source_Dataset` | Source dataset name |
| `Source_Variable_Name` | Original variable name in source |
| `Notes` | Mapping notes |

### Tier Classification
- **Tier 1 (Exact)**: Direct exact match (52 mappings)
- **Tier 2 (Synonym)**: Recognized synonym (28 mappings)
- **Tier 3 (Expert)**: Expert judgment required (9 mappings)

## Unit Harmonization Rules

### `unit_harmonization_rules.csv` Columns

| Column | Description |
|--------|-------------|
| `Variable_ID` | CVO variable ID |
| `Canonical_Unit` | Target canonical unit |
| `Source_Unit` | Source unit to convert from |
| `Conversion_Factor` | Multiplicative factor |
| `Conversion_Offset` | Additive offset |
| `Notes` | Conversion details |

**Formula**: `canonical_value = source_value * Conversion_Factor + Conversion_Offset`

Examples:
- `HWIN-VAR-001`: K = °C × 1 + 273.15
- `HWIN-VAR-003`: mol/m³ = mg/L × 0.03125 + 0.0
- `HWIN-VAR-005`: S/m = µS/cm × 0.0001 + 0.0

## Benchmark Protocol Parameters

### Frozen Protocol Values (DO NOT CHANGE)

| Parameter | Value | Location |
|-----------|-------|----------|
| `MIN_SAMPLES` | 100 | Protocol §4.2 |
| `MAX_SAMPLES` | 200,000 | Protocol §4.1 |
| `sampling_random_state` | 42 | Protocol §4.1 |
| `GroupKFold_n_splits` | 5 | Protocol §6.1 |
| `GroupKFold_group_var` | `station_id` | Protocol §6.1 |
| `seeds` | `[42, 123, 256, 512, 1024]` | Protocol §6.2 |
| `n_repetitions` | 5 | Protocol §6.1 |
| `feature_random_state` | N/A (deterministic) | Protocol §5 |
| `model_random_state` | 42 | Protocol §7 |
| `n_jobs` | -1 (for RF/ET/GB) | Protocol §7 |

### Feature Engineering (Protocol §5)

| Feature | Source | Transformation |
|---------|--------|----------------|
| `latitude` | `latitude` | Direct (float32) |
| `longitude` | `longitude` | Direct (float32) |
| `year` | `timestamp` | `dt.dt.year.fillna(2000).astype(int)` |
| `month` | `timestamp` | `dt.dt.month.fillna(6).astype(int)` |
| `day_of_year` | `timestamp` | `dt.dt.dayofyear.fillna(180).astype(int)` |
| `sin_doy` | `day_of_year` | `sin(2π × doy / 365.25)` |
| `cos_doy` | `day_of_year` | `cos(2π × doy / 365.25)` |

### Models (Protocol §7)

| Model | Class | Hyperparameters |
|-------|-------|-----------------|
| Linear Regression | `LinearRegression` | `{}` |
| Ridge | `Ridge` | `alpha=1.0` |
| Lasso | `Lasso` | `alpha=0.1, max_iter=5000` |
| ElasticNet | `ElasticNet` | `alpha=0.1, l1_ratio=0.5, max_iter=5000` |
| Random Forest | `RandomForestRegressor` | `n_estimators=200, max_depth=None, min_samples_split=2, random_state=42, n_jobs=-1` |
| Extra Trees | `ExtraTreesRegressor` | `n_estimators=200, max_depth=None, min_samples_split=2, random_state=42, n_jobs=-1` |
| Gradient Boosting | `GradientBoostingRegressor` | `n_estimators=200, learning_rate=0.1, max_depth=3, random_state=42` |

### Metrics (Protocol §8)

| Metric | Function | Formula |
|--------|----------|---------|
| MAE | `mean_absolute_error` | `mean(|y_true - y_pred|)` |
| RMSE | `root_mean_squared_error` | `sqrt(mean((y_true - y_pred)²))` |
| R² | `r2_score` | `1 - SS_res/SS_tot` (handles SS_tot=0) |
| MAPE | `mean_absolute_percentage_error` | `mean(|(y_true-y_pred)/y_true|)*100` (y_true≠0) |
| MedAE | `median_absolute_error` | `median(|y_true - y_pred|)` |

### Statistical Testing (Protocol §9.3)

| Test | Purpose | Correction |
|------|---------|------------|
| Kruskal-Wallis | Across all models per variable | — |
| Wilcoxon Signed-Rank | Pairwise model comparisons | Holm-Bonferroni |
| Cliff's Delta | Effect size for pairwise | — |
| Multiple Testing | 91 comparisons (7×13) | Holm-Bonferroni step-down |

### Confidence Intervals (Protocol §10)

| Parameter | Value |
|-----------|-------|
| Method | t-distribution |
| Confidence | 95% |
| Formula | `mean ± t_{0.975, n-1} × SEM` |
| Applied to | Mean of 5 unique fold evaluations per model-variable |

## Quality Flag Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | Good quality | Include |
| 1 | Suspect | Include with caution |
| 2 | Bad | Exclude |
| 3 | Below detection limit | Special handling |
| 4 | Above detection limit | Special handling |
| 9 | Missing | Exclude |

## Country Codes (ISO 3166-1 alpha-2)

Examples in GRQA: `AR` (Argentina), `AU` (Australia), `BR` (Brazil), `CA` (Canada), `CN` (China), `DE` (Germany), `FR` (France), `GB` (UK), `IN` (India), `US` (USA), and 59 others.

## Station Types

| Type | Description |
|------|-------------|
| `river` | River/stream monitoring station |
| `lake` | Lake/reservoir station |
| `estuary` | Estuarine station |
| `coastal` | Coastal marine station |
| `groundwater` | Groundwater well |
| `spring` | Spring |
| `wetland` | Wetland |
| `canal` | Canal/ditch |

---

**Version**: 1.0.0  
**Protocol**: Frozen v1.0 (see `benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md`)  
**Last Updated**: 2026-08-09