# Data Provenance — HWIN-Bench v1.0

Complete provenance chains for all five canonical datasets, from original source through HWIN-Bench representation to benchmark use.

> **Code-path note**: Path references of the form `src/hwin_bench/...` point to the
> original development repository (`HWIN_Bench_v1_RELEASE`), which produced the
> harmonized datasets shipped here. That pipeline is **not part of this public
> release**; the shipped `data/harmonized/` files are the canonical artifacts, and
> their SHA-256 checksums are recorded in `data/manifests/checksums.sha256`.

---

## Provenance Chain Overview

For each dataset, the provenance follows this standardized chain:

```
Original Source
    ↓
Download/Retrieval (URL, date, SHA256, authentication)
    ↓
Raw Representation (original format, structure, variables)
    ↓
Cleaning (quality filtering, missing data handling, deduplication)
    ↓
Harmonization (CVO variable mapping, unit conversion, CBS schema)
    ↓
Validation (CBS validation: completeness, range, referential integrity, duplicates, temporal, spatial)
    ↓
HWIN-Bench Representation (CBS-compliant observations, stations, variables, metadata)
    ↓
Benchmark Use (sampling, feature engineering, GroupKFold splits, model training, evaluation)
```

Each transition references the actual code or documented procedure.

---

## Dataset 1: HWIN-GRQA-V1-4 (Global River Quality Archive v1.4)

### Original Source
- **Publication**: Virro, H., Amatulli, G., Kmoch, A., Shen, L., & Uuemaa, E. (2021). *GRQA: Global River Water Quality Archive*. Earth System Science Data, 13, 5483–5507. https://doi.org/10.5194/essd-13-5483-2021
- **Data Repository**: Zenodo. GRQA v1.4. https://doi.org/10.5281/zenodo.15335450
- **Files**: 
  - `GRQA_data_v1.4.zip` (1.2 GB, md5:31617434a890b671f8f3a1eb342b2fbb)
  - `GRQA_meta_v1.4.zip` (44.8 MB, md5:89b885c4657e37ca43dcd2f566610d02)
  - `GRQA_figures_v1.4.zip` (38.1 MB)
  - `GRQA_source_data_v1.4.zip` (1.8 GB)
  - `README_v1.4.md` (3.1 KB)
  - `GRQA_data_catalog_v1.4.pdf` (26.2 MB)

### Download/Retrieval
- **Date**: 2026-07-08
- **Method**: Direct HTTPS download from Zenodo
- **Authentication**: None required (open access)
- **Verification**: MD5 checksums verified against Zenodo records
- **Code**: Manual download; see `scripts/archive/download_grqa.sh` (archived)

### Raw Representation
- **Format**: CSV files per variable (43 parameters) + metadata
- **Structure**: Station metadata, observation time series per parameter
- **Variables**: 43 water quality parameters (nutrients, carbon, oxygen, sediments)
- **Stations**: ~107,000 across 69 countries
- **Temporal**: 1894–2023
- **Observations**: ~17M in original GRQA; 25.8M after HWIN-Bench processing

### Cleaning
**Procedure**: GRQA pre-processing (Virro et al. 2021) + HWIN-Bench cleaning
- **Source cleaning** (GRQA pipeline): Outlier removal, unit standardization, duplicate removal across 5 source databases (CESI, GEMStat, GLORICH, Waterbase, WQP)
- **HWIN-Bench cleaning** (`src/hwin_bench/hwin_bench/canonicalization/engine.py`):
  - Remove observations with missing station_id, latitude, longitude, timestamp
  - Remove observations with missing or non-numeric values
  - Deduplicate by (station_id, timestamp, variable) keeping first
  - Filter impossible values (negative concentrations, pH outside 0-14, etc.)

### Harmonization
**Code**: `src/hwin_bench/hwin_bench/canonicalization/mapper.py` + `engine.py`
**Reference**: CVO v1.0 (`ontology/canonical_variable_ontology.csv`), Synonym Dictionary (`variable_synonym_dictionary.csv`), Unit Rules (`unit_harmonization_rules.csv`)

**Process per observation**:
1. **Variable Mapping**: Source parameter name → CVO ID via synonym dictionary (Tier 1→2→3 priority)
   - Example: GRQA `TEMP` → `HWIN-VAR-001` (Water Temperature) via Tier 1 exact match
   - 11 of 43 GRQA parameters map to benchmarkable CVO variables
2. **Unit Conversion**: Source unit → SI/canonical unit via unit harmonization rules
   - Example: `Deg C` → `K` (conversion: +273.15)
   - Example: `mg/L` → `mol/m³` (conversion: ×0.03125 for O₂)
3. **CBS Schema**: Restructure to CBS columns (observation_id, dataset_id, station_id, canonical_variable_id, value, unit, timestamp, latitude, longitude, country, site_name, param_name, source, quality_flag, percentile, original_value, original_unit, country_iso)
4. **Provenance Columns Added**:
   - `source_dataset`: Original GRQA source (GEMSTAT, WATERBASE, WQP, CESI, GLORICH)
   - `source_variable`: Original GRQA parameter code
   - `transformation_applied`: "unit_conversion" or "variable_mapping"
   - `conversion_factor`: Numeric factor used
   - `quality_flag_original`: GRQA quality flag

### Validation
**Code**: `src/hwin_bench/hwin_bench/canonicalization/engine.py` (CBS validation engine)
**Rules Applied** (58 total):
- **Completeness (8)**: Required columns present, no null station_id, no null coordinates, no null timestamps, no null values, no null canonical_variable_id, valid country codes, valid units
- **Range Validity (38)**: Per-variable physical limits (e.g., pH 0-14, temp -2 to 40°C, DO 0-20 mg/L, concentrations ≥0)
- **Referential Integrity (3)**: All station_ids in observations exist in stations.json, all canonical_variable_ids exist in variables.csv, all country codes ISO 3166-1 alpha-2
- **Duplicate Detection (2)**: No duplicate observation_ids, no duplicate (station_id, timestamp, canonical_variable_id)
- **Temporal Consistency (4)**: Timestamps parseable as ISO 8601, within dataset temporal coverage, chronological order per station-variable, no future dates
- **Spatial Consistency (3)**: Coordinates in valid ranges (lat -90 to 90, lon -180 to 180), country code matches coordinate location, station_type valid

**Certification**: Gold

### HWIN-Bench Representation
**Location**: `data/harmonized/HWIN-GRQA-V1-4/`
- `observations.csv`: 25,850,907 rows, CBS format (Note: GRQA observations.csv is in Zenodo due to GitHub LFS 2 GB limit)
- `stations.json`: 107,000 stations
- `variables.csv`: 11 canonical variables (11 benchmarkable after MIN_SAMPLES≥100)
- `dataset.json`: Metadata with checksums, DOI, coverage

**Key Metrics**:
- Canonical total observations: 25,800,000
- Benchmarked (MAX_SAMPLES=200K): 2,519,220
- Benchmarkable variables: 11 (MIN_SAMPLES≥100 in harmonized GRQA)

### Benchmark Use
**Code**: `benchmark/run_full_benchmark_fixed.py`
**Protocol**: Frozen v1.0 (`benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md`)

**Process**:
1. **Sampling**: Per variable, `sample(n=200000, random_state=42)` if >200K obs (10 of 11 variables)
2. **Feature Engineering**: 7 features (lat, lon, year, month, doy, sin_doy, cos_doy)
3. **Splits**: 5×5 GroupKFold by station_id, seeds [42, 123, 256, 512, 1024]
4. **Models**: 7 classical sklearn models with fixed hyperparameters
5. **Metrics**: MAE, RMSE, R², MAPE, MedAE per fold
6. **Aggregation**: Mean, Std, Median, 95% CI (t-distribution, n=5, df=4) across 5 unique fold evaluations (repeated 5 times deterministically)
6. **Statistics**: Kruskal-Wallis, Wilcoxon, Cliff's Delta, Holm-Bonferroni (not implemented in v1.0 — see Limitations)

**Output**: `output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete.json`

---

## Dataset 2: HWIN-WQP-SFBAY (Water Quality Portal — San Francisco Bay)

### Original Source
- **Provider**: U.S. Geological Survey (USGS) National Water Information System (NWIS) + Environmental Protection Agency (EPA) Water Quality Exchange (WQX)
- **Portal**: Water Quality Portal (WQP) — https://www.waterqualitydata.us/
- **Agencies**: 400+ state, federal, tribal, local agencies
- **License**: Public Domain (17 USC §105 — US Government works)

### Download/Retrieval
- **Date**: 2026-07-08
- **Method**: WQP REST API via Python requests
- **Query Parameters**:
  - `bbox=-123.5,37.0,-121.5,38.5` (San Francisco Bay bounding box)
  - `startDateLo=1950-01-01`, `startDateHi=2024-12-31`
  - `dataSource=NWIS,WQX`
  - `mimeType=csv`
- **Authentication**: None required
- **Code**: `examples/quickstart/download_wqp.py` (function `download_sfbay()`)
- **Volume**: ~51,000 observations retrieved

### Raw Representation
- **Format**: WQP CSV output (wide format with 100+ columns)
- **Key Columns**: `MonitoringLocationIdentifier`, `ActivityStartDate`, `CharacteristicName`, `ResultMeasureValue`, `ResultMeasureMeasureUnitCode`, `LatitudeMeasure`, `LongitudeMeasure`, `StateCode`, `CountyCode`, `OrganizationIdentifier`, `ActivityMediaName`, `ResultDetectionConditionText`, `ResultStatusIdentifier`, `StatisticalBaseCode`
- **Variables**: 19+ water quality characteristics
- **Stations**: ~1,000 monitoring locations

### Cleaning
**Code**: `src/hwin_bench/hwin_bench/loaders/wqp_loader.py` (archived)
**Process**:
1. Parse WQP CSV with robust encoding handling
2. Filter to `ResultStatusIdentifier == "Final"` and `ResultDetectionConditionText` not indicating non-detect (or handle censored data)
3. Remove rows missing: MonitoringLocationIdentifier, ActivityStartDate, CharacteristicName, ResultMeasureValue, LatitudeMeasure, LongitudeMeasure
4. Convert `ActivityStartDate` to ISO 8601 UTC
5. Deduplicate by (MonitoringLocationIdentifier, ActivityStartDate, CharacteristicName)

### Harmonization
**Code**: `src/hwin_bench/hwin_bench/canonicalization/mapper.py` + `engine.py`

**Variable Mapping** (WQP CharacteristicName → CVO):
| WQP Characteristic | CVO ID | Tier |
|---|---|---|
| "Temperature, water" | HWIN-VAR-001 | 1 (exact) |
| "pH" | HWIN-VAR-002 | 1 (exact) |
| "Dissolved oxygen (DO)" | HWIN-VAR-003 | 1 (exact) |
| "Dissolved oxygen saturation" | HWIN-VAR-014 | 1 (exact) |
| "Specific conductance" | HWIN-VAR-005 | 1 (exact) |
| "Nitrate" | HWIN-VAR-008 | 1 (exact) |
| "Nitrite" | HWIN-VAR-033 | 1 (exact) |
| "Ammonia" / "Ammonium" | HWIN-VAR-009 | 1 (exact) |
| "Orthophosphate" / "Phosphate-phosphorus" | HWIN-VAR-010 | 1 (exact) |
| "Chlorophyll a" | HWIN-VAR-011 | 1 (exact) |
| "Fecal Coliform" / "Escherichia coli" / "Enterococcus" | HWIN-VAR-012 | 1/2 |
| "Total suspended solids" | HWIN-VAR-015 | 1 (exact) |
| "Total dissolved solids" | HWIN-VAR-021 | 1 (exact) |
| "BOD" / "BOD5" | HWIN-VAR-022 | 1 (exact) |
| "COD" | HWIN-VAR-023 | 1 (exact) |
| "Alkalinity" | HWIN-VAR-020 | 1 (exact) |
| "Sulfate" | HWIN-VAR-018 | 1 (exact) |
| "Chloride" | HWIN-VAR-017 | 1 (exact) |
| "Silica" | HWIN-VAR-019 | 1 (exact) |
| "Flow" | HWIN-VAR-006 | 1 (exact) |
| "Depth" | HWIN-VAR-007 | 1 (exact) |

**Unit Conversion** (WQP units → SI):
- Temperature: °C → K (+273.15)
- DO: mg/L → mol/m³ (×0.03125)
- Specific Conductance: µS/cm → S/m (×0.0001)
- Nutrients: mg/L as N/P → mol/m³ (per variable molar mass)
- Flow: cfs → m³/s (×0.0283168)
- Depth: ft → m (×0.3048)

**Provenance Columns**:
- `source_dataset`: "WQP"
- `source_variable`: WQP CharacteristicName
- `transformation_applied`: "unit_conversion" + "variable_mapping"
- `conversion_factor`: As above
- `quality_flag_original`: WQP ResultStatusIdentifier/ResultDetectionConditionText

### Validation
**Code**: Same CBS validation engine as GRQA
**Certification**: Gold

### HWIN-Bench Representation
**Location**: `data/harmonized/HWIN-WQP-SFBAY/`
- `observations.csv`: 51,000 rows
- `stations.json`: 1,000+ stations
- `variables.csv`: 19 canonical variables
- `dataset.json`: Metadata

### Benchmark Use
- **Primary**: Transfer learning evaluation (Protocol §16) — train on GRQA subset matched to SF Bay region, evaluate on WQP SF Bay
- **Secondary**: Data heterogeneity demonstration
- **Not used**: Canonical regression benchmark (GRQA only per Protocol §3.3)

---

## Dataset 3: HWIN-STORET-CA (EPA STORET California)

### Original Source
- **Provider**: U.S. Environmental Protection Agency (EPA) STORET Warehouse / Water Quality Exchange (WQX)
- **Portal**: https://www.epa.gov/waterdata/storage-and-retrieval-and-water-quality-exchange
- **Accessed via**: Water Quality Portal (WQP) API
- **License**: Public Domain (17 USC §105)

### Download/Retrieval
- **Date**: 2026-07-08
- **Method**: WQP REST API
- **Query Parameters**:
  - `statecode=US:06` (California FIPS code)
  - `startDateLo=1950-01-01`, `startDateHi=2024-12-31`
  - `dataSource=WQX` (EPA STORET/WQX only)
- **Code**: `examples/quickstart/download_wqp.py` (function `download_storet_state()`)
- **Volume**: ~180,000 observations

### Raw Representation
- **Format**: WQP CSV (same structure as WQP SF Bay)
- **Source**: EPA WQX (STORET) database
- **Stations**: ~3,000 monitoring locations in California

### Cleaning
Same as WQP SF Bay (shared loader code)

### Harmonization
**Variable Mapping**: Same WQP CharacteristicName → CVO mapping as SF Bay
- 22 canonical variables mapped
- STORET-specific parameter codes also mapped via synonym dictionary (STORET entries: 00010=Temp, 00300=DO, 00400=pH, 00610=Ammonia, 00620=Nitrate, 00665=Phosphorus, 00940=Chloride, 00945=Sulfate, 00094=SpCond, 00070=Turbidity, 00530=TSS, 00310=BOD5, 00340=COD, 00410=Alkalinity, 00955=Silica, 32211=Chlorophyll-a, 31616=Fecal Coliform)

**Unit Conversion**: Same as WQP (STORET data served via WQP uses standard units)

### Validation
Same CBS validation engine
**Certification**: Gold

### HWIN-Bench Representation
**Location**: `data/harmonized/HWIN-STORET-CA/`
- `observations.csv`: 180,000 rows
- `stations.json`: 3,000 stations
- `variables.csv`: 22 canonical variables
- `dataset.json`: Metadata

### Benchmark Use
- **Primary**: Transfer learning evaluation (Protocol §16) — train on GRQA California-matched subset, evaluate on STORET CA
- **Not used**: Canonical regression benchmark

---

## Dataset 4: HWIN-STORET-TX (EPA STORET Texas)

### Original Source
- **Provider**: EPA STORET/WQX via WQP
- **License**: Public Domain (17 USC §105)

### Download/Retrieval
- **Date**: 2026-07-08
- **Method**: WQP REST API
- **Query**: `statecode=US:48` (Texas FIPS), `dataSource=WQX`, 1950-2024
- **Volume**: ~175,000 observations, ~2,000 stations

### Processing
Identical to STORET CA (shared pipeline)

### Harmonization
- 21 canonical variables
- Same variable/unit mappings

### Validation
CBS validation — Gold

### HWIN-Bench Representation
**Location**: `data/harmonized/HWIN-STORET-TX/`

### Benchmark Use
Transfer learning evaluation (GRQA Texas-matched → STORET TX)

---

## Dataset 5: HWIN-STORET-RI (EPA STORET Rhode Island)

### Original Source
- **Provider**: EPA STORET/WQX via WQP
- **License**: Public Domain (17 USC §105)

### Download/Retrieval
- **Date**: 2026-07-08
- **Method**: WQP REST API
- **Query**: `statecode=US:44` (Rhode Island FIPS), `dataSource=WQX`, 1950-2024
- **Volume**: ~2,500 observations, ~50 stations

### Processing
Identical pipeline

### Harmonization
- 18 canonical variables
- Same mappings

### Validation
CBS validation — Gold

### HWIN-Bench Representation
**Location**: `data/harmonized/HWIN-STORET-RI/`

### Benchmark Use
Transfer learning evaluation (GRQA Northeast-matched → STORET RI)

---

## Cross-Cutting Provenance Elements

### Canonical Variable Ontology (CVO v1.0)
- **Source**: Expert curation by HWIN-Bench team
- **File**: `ontology/canonical_variable_ontology.csv`
- **Process**: Literature review of water quality parameters across 7 major monitoring programs (GEMStat, WQP, NEON, GLORIA, QUADICA, GRQA, STORET) → consolidate to 49 canonical variables with definitions, synonyms, units, ranges
- **Version**: 1.0 (frozen for v1.0)
- **License**: CC0-1.0 (original expert curation)

### Variable Synonym Dictionary
- **Source**: Expert mapping by HWIN-Bench team
- **File**: `ontology/variable_synonym_dictionary.csv`
- **Process**: For each source dataset, map every parameter name to CVO ID using Tier 1/2/3 classification
- **Entries**: 89 mappings (52 Tier 1, 28 Tier 2, 9 Tier 3)
- **License**: CC0-1.0

### Unit Harmonization Rules
- **Source**: Physical constants, standard conversion factors
- **File**: `ontology/unit_harmonization_rules.csv`
- **Process**: For each CVO variable, document all source units encountered and conversion to SI/canonical unit
- **Entries**: 92 rules
- **License**: CC0-1.0

### Canonical Benchmark Schema (CBS)
- **Source**: HWIN-Bench design
- **Code**: `src/hwin_bench/hwin_bench/canonicalization/engine.py` (CBS definition)
- **Schema**: Observations, Stations, Variables, Dataset metadata as specified in `docs/DATA_DICTIONARY.md`
- **License**: CC0-1.0

---

## Provenance Summary Table

| Dataset | Original Source | Retrieval Date | Retrieval Method | Cleaning Code | Harmonization Code | Validation Code | CBS Certification |
|---------|----------------|----------------|------------------|---------------|-------------------|-----------------|-------------------|
| HWIN-GRQA-V1-4 | Zenodo (doi:10.5281/zenodo.15335450) | 2026-07-08 | HTTPS download | `canonicalization/engine.py` | `canonicalization/mapper.py` + `engine.py` | `canonicalization/engine.py` | Gold |
| HWIN-WQP-SFBAY | WQP API | 2026-07-08 | REST API (bbox) | `loaders/wqp_loader.py` | `canonicalization/mapper.py` + `engine.py` | `canonicalization/engine.py` | Gold |
| HWIN-STORET-CA | WQP API | 2026-07-08 | REST API (statecode=US:06) | `loaders/wqp_loader.py` | `canonicalization/mapper.py` + `engine.py` | `canonicalization/engine.py` | Gold |
| HWIN-STORET-TX | WQP API | 2026-07-08 | REST API (statecode=US:48) | `loaders/wqp_loader.py` | `canonicalization/mapper.py` + `engine.py` | `canonicalization/engine.py` | Gold |
| HWIN-STORET-RI | WQP API | 2026-07-08 | REST API (statecode=US:44) | `loaders/wqp_loader.py` | `canonicalization/mapper.py` + `engine.py` | `canonicalization/engine.py` | Gold |

---

## Benchmark Provenance

### Canonical Execution
- **Script**: `benchmark/run_full_benchmark_fixed.py` (ONLY)
- **Protocol**: `benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md` (frozen v1.0)
- **Date**: 2026-07-24
- **Duration**: 15.5 hours (wall-clock)
- **Hardware**: CPU (8-core), 32 GB RAM
- **Environment**: Python 3.11, scikit-learn 1.5.x, numpy 1.26.x, pandas 2.2.x
- **Seeds**: [42, 123, 256, 512, 1024] (GroupKFold), 42 (sampling, models)
- **Output**: `output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete.json`

### Reproducibility Verification
- **Independent reproduction**: Completed 2026-07-24
- **Certificate**: `benchmark/reproducibility/CANONICAL_EXECUTION_CERTIFICATE.md`
- **Log**: `EXECUTION_LOG.md`
- **Verification**: `REPRODUCIBILITY_VERIFICATION.md`

---

## Version Control

All code referenced above is from the **HWIN-Bench** repository (https://github.com/Zakariya-Q/HWIN-Bench) at the tagged commit for v1.0.

**Tag**: `v1.0.0` 
**Key Commit**: Canonical pipeline freeze after COMP-006 fix (GroupKFold correction)

---

## Contact

For provenance questions or corrections, open a GitHub Issue with label `provenance`.

---

**Version**: 1.0.0  
**Protocol**: Frozen v1.0  
**Last Updated**: 2026-08-11