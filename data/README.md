# HWIN-Bench v1.0 — Data Directory

This directory contains all data artifacts for the HWIN-Bench v1.0 public release.

## Directory Structure

```
data/
├── README.md              # This file
├── datasets/              # Raw source datasets (where redistribution permitted)
├── metadata/              # Dataset metadata (dataset.json, stations.json, variables.csv)
├── harmonized/            # CBS-harmonized datasets (READY FOR BENCHMARK)
├── manifests/             # Checksums and manifests
└── README.md              # This file
```

## What's Included

### Raw Source Datasets (`datasets/`)

All 5 canonical source datasets are included in their original downloaded form where licenses permit redistribution:

| Dataset | License | Included? | Size |
|---------|---------|-----------|------|
| GRQA v1.4 | CC-BY-4.0 | ✅ Yes | ~6.0 GB |
| WQP SF Bay | Public Domain | ✅ Yes | ~4.6 MB |
| STORET CA | Public Domain | ✅ Yes | ~42.7 MB |
| STORET TX | Public Domain | ✅ Yes | ~46.5 MB |
| STORET RI | Public Domain | ✅ Yes | ~0.5 MB |

**Note**: GRQA v1.4 is downloaded from Zenodo (doi:10.5281/zenodo.15335450). WQP/STORET datasets are extracted via the Water Quality Portal API as accessed on 2026-07-08.

### Metadata (`metadata/`)

Each dataset includes standardized metadata following ISO 19115-3:

```
metadata/
├── HWIN-GRQA-V1-4/
│   ├── dataset.json       # Dataset-level metadata (license, DOI, coverage, checksums)
│   ├── stations.json      # Station metadata (107,000 stations)
│   └── variables.csv      # Variable definitions (11 canonical variables)
├── HWIN-WQP-SFBAY/
│   ├── dataset.json
│   ├── stations.json      # 1,000+ stations
│   └── variables.csv      # 19 canonical variables
├── HWIN-STORET-CA/
│   ├── dataset.json
│   ├── stations.json      # 3,000 stations
│   └── variables.csv      # 22 canonical variables
├── HWIN-STORET-TX/
│   ├── dataset.json
│   ├── stations.json      # 2,000 stations
│   └── variables.csv      # 21 canonical variables
└── HWIN-STORET-RI/
    ├── dataset.json
    ├── stations.json      # 50 stations
    └── variables.csv      # 18 canonical variables
```

### Harmonized Datasets (`harmonized/`)

**These are the primary datasets for benchmark execution.** All 5 datasets are mapped to the **Canonical Benchmark Schema (CBS)** with:

- **Canonical Variable IDs** (HWIN-VAR-XXX) from the CVO
- **SI Units** applied via unit harmonization rules
- **Quality flags** preserved from source
- **Provenance columns**: source_dataset, source_variable, transformation_applied, conversion_factor, quality_flag_original

```
harmonized/
├── HWIN-GRQA-V1-4/
│   ├── observations.csv      # 25.8M observations, CBS format
│   ├── stations.json         # Station metadata
│   ├── variables.csv         # Canonical variable definitions
│   └── dataset.json          # Dataset metadata
├── HWIN-WQP-SFBAY/
│   ├── observations.csv      # 51K observations
│   ├── stations.json
│   ├── variables.csv
│   └── dataset.json
├── HWIN-STORET-CA/
│   ├── observations.csv      # 180K observations
│   ├── stations.json
│   ├── variables.csv
│   └── dataset.json
├── HWIN-STORET-TX/
│   ├── observations.csv      # 175K observations
│   ├── stations.json
│   ├── variables.csv
│   └── dataset.json
└── HWIN-STORET-RI/
    ├── observations.csv      # 2.5K observations
    ├── stations.json
    ├── variables.csv
    └── dataset.json
```

**CBS Observation Format:**
```csv
observation_id,dataset_id,station_id,canonical_variable_id,value,unit,timestamp,latitude,longitude,country,site_name,param_name,source,quality_flag,percentile,original_value,original_unit,country_iso
```

### Manifests (`manifests/`)

```
manifests/
├── checksums.sha256          # SHA256 for all files in data/
├── file_inventory.csv        # Complete file listing with sizes
└── dataset_versions.csv      # Version tracking per dataset
```

## Verifying Integrity

```bash
# Verify all checksums
cd data/
sha256sum -c manifests/checksums.sha256

# Quick verification of key files
sha256sum harmonized/HWIN-GRQA-V1-4/observations.csv
sha256sum harmonized/HWIN-WQP-SFBAY/observations.csv
```

## Downloading Fresh Copies

For production use, we recommend downloading fresh from original providers:

### GRQA v1.4 (Required for canonical benchmark)
```bash
# From Zenodo (official release)
wget https://zenodo.org/records/15335450/files/GRQA_data_v1.4.zip
wget https://zenodo.org/records/15335450/files/GRQA_meta_v1.4.zip
wget https://zenodo.org/records/15335450/files/README_v1.4.md

# Expected checksums (from Zenodo):
# GRQA_data_v1.4.zip: md5:31617434a890b671f8f3a1eb342b2fbb
# GRQA_meta_v1.4.zip: md5:89b885c4657e37ca43dcd2f566610d02
```

### WQP / STORET (via Water Quality Portal API)
```bash
# See examples/quickstart/download_wqp.py for full script
# Key parameters for HWIN-Bench v1.0 subsets:
# - SF Bay: bbox=-123.5,37.0,-121.5,38.5
# - California: statecode=US:06
# - Texas: statecode=US:48
# - Rhode Island: statecode=US:44
# - Date range: 1950-01-01 to 2024-12-31
# - Data sources: NWIS (USGS) + WQX (EPA)
```

## Version Requirements for Reproduction

To exactly reproduce HWIN-Bench v1.0 results, you MUST use:

| Dataset | Version | Access Date | Source |
|---------|---------|-------------|--------|
| GRQA | v1.4 | 2026-07-08 | Zenodo doi:10.5281/zenodo.15335450 |
| WQP SF Bay | As accessed | 2026-07-08 | Water Quality Portal API |
| STORET CA | As accessed | 2026-07-08 | Water Quality Portal API |
| STORET TX | As accessed | 2026-07-08 | Water Quality Portal API |
| STORET RI | As accessed | 2026-07-08 | Water Quality Portal API |

**The benchmark will fail loudly if the wrong dataset version is supplied.** The validation step checks dataset_id, version, and observation counts against the frozen protocol.

## Data Provenance

Full provenance chains documented in `../docs/DATA_PROVENANCE.md`:

```
Original Source → Download (URL, date, SHA256) → Extraction → 
Canonicalization (CVO mapping + unit conversion) → CBS Validation → 
Split Generation → Benchmark Execution
```

Per-observation provenance in CBS: `source_dataset`, `source_variable`, `transformation_applied`, `conversion_factor`, `quality_flag_original`.

## Licenses

| Dataset | License | Redistribution |
|---------|---------|----------------|
| GRQA v1.4 | CC-BY-4.0 | ✅ Permitted with attribution |
| WQP/STORET | Public Domain (17 USC 105) | ✅ Permitted, no restrictions |

See `../licenses/DATASET_LICENSE_AUDIT.csv` for full audit.
See `../licenses/ATTRIBUTION.md` for required attribution text.

## Storage Requirements

| Dataset | Raw | Harmonized | Total |
|---------|-----|------------|-------|
| GRQA v1.4 | 6.0 GB | 2.0 GB | 8.0 GB |
| WQP SF Bay | 4.6 MB | 4.6 MB | 9.2 MB |
| STORET CA | 42.7 MB | 42.7 MB | 85.4 MB |
| STORET TX | 46.5 MB | 46.5 MB | 93.0 MB |
| STORET RI | 0.5 MB | 0.5 MB | 1.0 MB |
| **Total** | **~6.1 GB** | **~2.1 GB** | **~8.2 GB** |

---

**Note**: The `harmonized/` datasets are the **canonical input** for the benchmark. The benchmark runner (`benchmark/run_full_benchmark_fixed.py`) expects data in this CBS format.