# Data Guide — HWIN-Bench v1.0

Complete reference for accessing, understanding, and using HWIN-Bench data.

## Overview

HWIN-Bench v1.0 uses **5 canonical datasets** harmonized to a common **Canonical Benchmark Schema (CBS)**. All data is provided in two forms:
1. **Raw source data** (`data/datasets/`) — as downloaded from original providers
2. **Harmonized CBS data** (`data/harmonized/`) — ready for benchmark execution

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

### Variables (`variables.csv`)

```csv
canonical_variable_id,canonical_name,definition,si_unit,preferred_datatype,expected_range
HWIN-VAR-001,Water Temperature,The intensity of heat present in water,K,Float,-2 to 40 deg C
```

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

## The Five Datasets

### 1. HWIN-GRQA-V1-4 — Global River Quality Archive v1.4

**Source**: Zenodo (doi:10.5281/zenodo.15335450)  
**License**: CC-BY-4.0  
**Coverage**: Global, 69 countries, 107,000 stations, 1894-2023  
**Variables**: 11 canonical (11 benchmarkable after MIN_SAMPLES filter)  
**Observations**: 25.8M canonical, 2.5M benchmarked (MAX_SAMPLES=200K cap)

**Benchmarkable Variables** (MIN_SAMPLES ≥ 100):
- HWIN-VAR-001: Water Temperature (5.5M obs)
- HWIN-VAR-002: pH (4.7M obs)
- HWIN-VAR-003: Dissolved Oxygen (2.8M obs)
- HWIN-VAR-008: Nitrate Nitrogen (2.3M obs)
- HWIN-VAR-009: Ammonium Nitrogen (1.0M obs)
- HWIN-VAR-010: Phosphate Phosphorus (2.9M obs)
- HWIN-VAR-014: DO Percent Saturation (1.7M obs)
- HWIN-VAR-015: Total Suspended Solids (1.3M obs)
- HWIN-VAR-028: Total Nitrogen (1.8M obs)
- HWIN-VAR-031: Total Ammonia Nitrogen (0.6M obs)
- HWIN-VAR-033: Nitrite Nitrogen (1.3M obs)

### 2. HWIN-WQP-SFBAY — Water Quality Portal: San Francisco Bay

**Source**: Water Quality Portal API (bbox: -123.5,37.0,-121.5,38.5)  
**License**: Public Domain (USGS NWIS + EPA WQX)  
**Coverage**: San Francisco Bay, CA, USA; 1,000+ stations, 1950-2024  
**Variables**: 19 canonical  
**Observations**: 51K total

**Variables**: pH, Water Depth, Dissolved Oxygen, Phosphate Phosphorus, Total Dissolved Solids, Sulfate, Silica, Nitrate Nitrogen, Fecal Coliforms, Alkalinity, Chlorophyll-a, Flow Rate, Total Suspended Solids, Chloride, Specific Conductance, Water Temperature, Turbidity, Ammonium Nitrogen

### 3. HWIN-STORET-CA — EPA STORET California

**Source**: Water Quality Portal API (statecode=US:06)  
**License**: Public Domain (EPA STORET/WQX)  
**Coverage**: California, USA; 3,000 stations, 1950-2024  
**Variables**: 22 canonical  
**Observations**: 180K total

### 4. HWIN-STORET-TX — EPA STORET Texas

**Source**: Water Quality Portal API (statecode=US:48)  
**License**: Public Domain (EPA STORET/WQX)  
**Coverage**: Texas, USA; 2,000 stations, 1950-2024  
**Variables**: 21 canonical  
**Observations**: 175K total

### 5. HWIN-STORET-RI — EPA STORET Rhode Island

**Source**: Water Quality Portal API (statecode=US:44)  
**License**: Public Domain (EPA STORET/WQX)  
**Coverage**: Rhode Island, USA; 50 stations, 1950-2024  
**Variables**: 18 canonical  
**Observations**: 2.5K total

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

## Data Access Patterns

### Loading in Python

```python
import pandas as pd
import json

# Load harmonized observations
obs = pd.read_csv('data/harmonized/HWIN-GRQA-V1-4/observations.csv')

# Load stations
with open('data/harmonized/HWIN-GRQA-V1-4/stations.json') as f:
    stations = json.load(f)

# Load variables
vars = pd.read_csv('data/harmonized/HWIN-GRQA-V1-4/variables.csv')

# Load dataset metadata
with open('data/harmonized/HWIN-GRQA-V1-4/dataset.json') as f:
    meta = json.load(f)

# Filter for benchmarkable variable
temp_data = obs[obs['canonical_variable_id'] == 'HWIN-VAR-001']
```

### Using the HWIN-Bench Loader

```python
from hwin_bench import load_dataset

# Load canonical GRQA dataset for benchmark
ds = load_dataset('HWIN-GRQA-V1-4', root='data/harmonized')
# Returns: observations DataFrame, stations list, variables DataFrame, metadata dict
```

## Verification Checklist

Before running benchmark, verify:

- [ ] All 5 dataset directories exist in `data/harmonized/`
- [ ] Each has `observations.csv`, `stations.json`, `variables.csv`, `dataset.json`
- [ ] Checksums match `data/manifests/checksums.sha256`
- [ ] GRQA has 11 benchmarkable variables (MIN_SAMPLES ≥ 100)
- [ ] Observation counts match `DATASET_RELEASE_INVENTORY.csv`
- [ ] Column names match CBS specification exactly

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Missing `canonical_variable_id` | Source variable not in synonym dictionary | Check `ontology/variable_synonym_dictionary.csv` |
| Unit conversion failed | Source unit not in harmonization rules | Check `ontology/unit_harmonization_rules.csv` |
| Station ID mismatch | Station metadata not aligned | Re-run metadata alignment |
| MemoryError loading GRQA | 25.8M rows too large for RAM | Use chunked reading or database |

## Citation

When using these data, cite both HWIN-Bench and the original datasets:

```bibtex
@software{hwin_bench_v1,
  title = {HWIN-Bench v1.0},
  doi = {10.5281/zenodo.21877825}
}

@dataset{grqa_v14,
  title = {Global River Water Quality Archive (GRQA) v1.4},
  author = {Virro et al.},
  year = {2025},
  doi = {10.5281/zenodo.15335450}
}
```

See `../licenses/ATTRIBUTION.md` for full attribution requirements.