# Data README — HWIN-Bench v1.0

## Overview

The `data/` directory contains all dataset-related files for HWIN-Bench v1.0.

## Structure

```
data/
├── harmonized/              # Harmonized CBS datasets (5 datasets)
│   ├── HWIN-GRQA-V1-4/
│   │   ├── dataset.json
│   │   ├── stations.json
│   │   ├── variables.csv
│   │   └── observations.csv  # NOTE: GRQA observations.csv is in Zenodo (5.7 GB)
│   ├── HWIN-WQP-SFBAY/
│   │   ├── dataset.json
│   │   ├── stations.json
│   │   ├── variables.csv
│   │   └── observations.csv
│   ├── HWIN-STORET-CA/
│   │   ├── dataset.json
│   │   ├── stations.json
│   │   ├── variables.csv
│   │   └── observations.csv
│   ├── HWIN-STORET-TX/
│   │   ├── dataset.json
│   │   ├── stations.json
│   │   ├── variables.csv
│   │   └── observations.csv
│   └── HWIN-STORET-RI/
│       ├── dataset.json
│       ├── stations.json
│       ├── variables.csv
│       └── observations.csv
├── manifests/
│   ├── checksums.sha256
│   ├── DATASET_RELEASE_INVENTORY.csv
│   └── DERIVED_DATA_AUDIT.csv
└── README.md (this file)
```

---

## GRQA v1.4 Data Note

**Important**: The GRQA v1.4 `observations.csv` file (5.7 GB) **is not included in this GitHub repository** because it exceeds GitHub's 2 GB per-file LFS limit.

### How to Obtain GRQA observations.csv

1. **Download from Zenodo** (recommended for reproducibility):
   ```bash
   wget https://zenodo.org/records/15335450/files/GRQA_data_v1.4.zip
   unzip GRQA_data_v1.4.zip
   # Place observations.csv in data/harmonized/HWIN-GRQA-V1-4/
   ```

2. **Use the Quickstart Smoke Test** (for quick validation without full data):
   ```bash
   cd benchmark
   python run_full_benchmark_fixed.py --smoke-test
   ```

3. **Verify Checksum** after download:
   ```bash
   sha256sum data/harmonized/HWIN-GRQA-V1-4/observations.csv
   # Should match: 989e5a6ba07499d81443c8819ef7f1e786fdef8a52661474a2bf5cc4a2ed6f8f
   ```

---

## Dataset Sizes

| Dataset | observations.csv | stations.json | variables.csv | dataset.json |
|---------|------------------|---------------|---------------|--------------|
| GRQA v1.4 | 5.7 GB (Zenodo) | 23 MB | 1.9 KB | 2.1 KB |
| WQP SF Bay | 4.6 MB | 24 MB | 1.9 KB | 2.1 KB |
| STORET CA | 41 MB | 13 MB | 1.9 KB | 2.1 KB |
| STORET TX | 45 MB | 13 MB | 1.9 KB | 2.1 KB |
| STORET RI | 0.5 MB | 1.3 MB | 1.9 KB | 2.1 KB |

---

## Manifests

- `manifests/checksums.sha256` — SHA256 checksums for all files
- `manifests/DATASET_RELEASE_INVENTORY.csv` — Dataset inventory with row counts, column counts, sizes
- `manifests/DERIVED_DATA_AUDIT.csv` — Audit of derived data artifacts

---

## Verification

```bash
# Verify all checksums
cd data/
sha256sum -c manifests/checksums.sha256

# Check dataset properties
python -c "
import pandas as pd
obs = pd.read_csv('harmonized/HWIN-GRQA-V1-4/observations.csv')
print(f'GRQA observations: {len(obs)}')
print(f'GRQA variables: {obs.canonical_variable_id.nunique()}')
print(f'GRQA stations: {obs.station_id.nunique()}')
vars = pd.read_csv('harmonized/HWIN-GRQA-V1-4/variables.csv')
print(f'Benchmarkable vars (MIN_SAMPLES>=100): {len(vars)}')
"
```

---

## License

Individual datasets retain their original licenses:
- GRQA v1.4: CC-BY-4.0
- WQP/STORET: Public Domain (17 USC §105)

See `licenses/DATASET_LICENSE_AUDIT.csv` for full audit.