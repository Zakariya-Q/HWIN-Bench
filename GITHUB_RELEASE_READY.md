# GitHub Release Preparation — HWIN-Bench v1.0

Complete guide for creating the HWIN-Bench v1.0 GitHub repository and release.

---

## Repository Details

| Property | Value |
|----------|-------|
| **Repository Name** | `HWIN-Bench-v1.0` |
| **Organization** | `HWIN-Bench` (to be created) |
| **Visibility** | Public |
| **Default Branch** | `main` |
| **Release Tag** | `v1.0.0` |
| **Release Title** | `HWIN-Bench v1.0.0 — Public Release` |
| **Target Branch** | `main` |
| **Pre-release** | No |

---

## Repository Structure (Files to Commit)

### Core Files (Always in Git)
```
README.md                          # 11 KB
LICENSE                            # 17 KB
CITATION.cff                       # 3 KB
CHANGELOG.md                       # 4 KB
.gitattributes                     # 1 KB (Git LFS config)
.gitignore                         # 1 KB
```

### Code (src/, benchmark/, tests/)
```
src/
  hwin_bench/                      # Full package
    cli.py
    hwin_bench/
      __init__.py
      cli.py
      canonicalization/            # 12 modules
      baselines/                   # 7 modules
      evaluation/                  # 4 modules
      loaders/                     # 4 modules
      runner/                      # 3 modules
      tasks/                       # 3 modules
      validation/                  # 3 modules
      leaderboard/                 # 3 modules
benchmark/
  protocol/
    01_HWIN_BENCH_PROTOCOL_v1.0.md # 14 KB (frozen)
  run_full_benchmark_fixed.py      # 25 KB (canonical runner)
  __init__.py
code/
  benchmark/
    run_full_benchmark_fixed.py    # 25 KB (copy for release)
  validation/
    cbs_validator.py               # 15 KB
  requirements/
    requirements.txt               # 1.5 KB
    environment.yml                # 3 KB
tests/                             # 74 tests
```

### Documentation (docs/)
```
docs/
  QUICKSTART.md                    # 3 KB
  DATA_GUIDE.md                    # 9 KB
  DATA_DICTIONARY.md               # 10 KB
  REPRODUCIBILITY.md               # 7 KB
  LIMITATIONS.md                   # 9 KB
  DATA_PROVENANCE.md               # 18 KB
```

### Ontology (ontology/)
```
ontology/
  canonical_variable_ontology.csv  # 18 KB
  variable_synonym_dictionary.csv  # 33 KB
  unit_harmonization_rules.csv     # 6 KB
```

### Data Manifests (data/manifests/)
```
data/
  README.md                        # 7 KB
  manifests/
    checksums.sha256               # 1 KB (to be computed)
    file_inventory.csv             # 2 KB
    dataset_versions.csv           # 1 KB
    DATASET_RELEASE_INVENTORY.csv  # 2 KB
    DERIVED_DATA_AUDIT.csv         # 7 KB
```

### Licenses (licenses/)
```
licenses/
  DATASET_LICENSE_AUDIT.csv        # 6 KB
  ATTRIBUTION.md                   # 8 KB
```

### Examples (examples/)
```
examples/
  quickstart/
    download_wqp.py                # 5 KB
    analyze_results.ipynb          # 15 KB
  __init__.py
```

### Benchmark Results (benchmark/results/, benchmark/reproducibility/)
```
benchmark/
  results/
    .gitkeep
  reproducibility/
    CANONICAL_EXECUTION_CERTIFICATE.md  # 6 KB
    REPRODUCIBILITY_VERIFICATION.md     # 5 KB
    EXECUTION_LOG.md                    # 6 KB
```

### Release Audit Files (Root)
```
REDISTRIBUTION_DECISIONS.md        # 9 KB
PUBLIC_RELEASE_VALIDATION.md       # 7 KB
PUBLIC_RELEASE_READINESS.md        # 6 KB
PUBLIC_RELEASE_MANIFEST.csv        # 15 KB
GITHUB_RELEASE_READY.md            # This file
```

---

## Files Requiring Git LFS (Large Files)

| File | Size | LFS Required |
|------|------|--------------|
| `data/harmonized/HWIN-GRQA-V1-4/observations.csv` | 6.0 GB | **YES** |
| `data/datasets/HWIN-GRQA-V1-4/GRQA_data_v1.4.zip` | 1.2 GB | **YES** |
| `data/datasets/HWIN-GRQA-V1-4/GRQA_meta_v1.4.zip` | 44.8 MB | Recommended |
| `data/harmonized/HWIN-STORET-CA/observations.csv` | 42.7 MB | Recommended |
| `data/harmonized/HWIN-STORET-TX/observations.csv` | 46.5 MB | Recommended |

### .gitattributes Configuration
```gitattributes
# Git LFS for large data files
data/harmonized/HWIN-GRQA-V1-4/observations.csv filter=lfs diff=lfs merge=lfs -text
data/datasets/HWIN-GRQA-V1-4/GRQA_data_v1.4.zip filter=lfs diff=lfs merge=lfs -text
data/datasets/HWIN-GRQA-V1-4/GRQA_meta_v1.4.zip filter=lfs diff=lfs merge=lfs -text
data/harmonized/HWIN-STORET-CA/observations.csv filter=lfs diff=lfs merge=lfs -text
data/harmonized/HWIN-STORET-TX/observations.csv filter=lfs diff=lfs merge=lfs -text

# Explicitly track as text
*.md text
*.csv text
*.py text
*.yml text
*.txt text
*.cff text
*.json text
```

---

## Expected Repository Size

| Component | Size |
|-----------|------|
| Git-tracked files (code, docs, ontology, manifests) | ~4 MB |
| Git LFS files (3 files) | ~7.3 GB |
| **Total repository size** | **~7.3 GB** |
| **GitHub storage** | Within limits (Git LFS free tier: 1 GB/file, 1 GB/month bandwidth; may need paid for 6 GB file) |

**Note**: The 6 GB GRQA observations.csv exceeds GitHub's 2 GB/file limit for standard Git, but Git LFS supports up to 5 GB/file on free tier. For 6 GB, you may need:
- Git LFS paid plan, OR
- Split the file into chunks, OR
- Host GRQA data on Zenodo only and provide download script

**Recommendation**: Host GRQA raw/harmonized data on Zenodo (already at doi:10.5281/zenodo.15335450) and include only the smaller STORET/WQP datasets in GitHub. Provide download script for GRQA.

---

## Files EXCLUDED from Release (Do Not Commit)

| Excluded Path | Reason |
|---------------|--------|
| `archive/` | Internal audit files |
| `scripts/archive/` | Legacy scripts |
| `output/` (except benchmark/results/) | Generated artifacts |
| `.pytest_cache/`, `__pycache__/` | Build cache |
| `*.bak`, `*.new` | Backup files |
| `AUDIT_*.md`, `BLOCKER_*.md` | Internal process |
| `HWIN_MANUSCRIPT_SOURCE_v1.0/` | Manuscript (separate) |
| `HWIN_Bench_v1_PUBLICATION/` | Publication package |
| `ZENODO_RELEASE/` | Zenodo deposit package |
| `*.key`, `*.pem`, `.env` | Secrets (none present) |
| Internal absolute paths | Privacy |

---

## Release Creation Steps

### 1. Initialize Repository
```bash
cd HWIN_Bench_v1_PUBLIC_RELEASE
git init
git remote add origin https://github.com/HWIN-Bench/HWIN-Bench-v1.0.git
```

### 2. Configure Git LFS
```bash
git lfs install
git lfs track "data/harmonized/HWIN-GRQA-V1-4/observations.csv"
git lfs track "data/datasets/HWIN-GRQA-V1-4/GRQA_data_v1.4.zip"
git lfs track "data/datasets/HWIN-GRQA-V1-4/GRQA_meta_v1.4.zip"
git lfs track "data/harmonized/HWIN-STORET-CA/observations.csv"
git lfs track "data/harmonized/HWIN-STORET-TX/observations.csv"
git add .gitattributes
```

### 3. Compute Checksums
```bash
cd data/
sha256sum harmonized/*/observations.csv harmonized/*/stations.json harmonized/*/variables.csv harmonized/*/dataset.json datasets/*/* > manifests/checksums.sha256
```

### 4. Commit and Push
```bash
git add .
git commit -m "HWIN-Bench v1.0.0 — Public Release

- Frozen benchmark protocol v1.0
- 5 canonical datasets (GRQA, WQP-SFBay, STORET-CA/TX/RI)
- Canonical Variable Ontology (51 variables)
- 7 classical ML models, 5×5 GroupKFold, 2,275 model fits
- Full statistical rigor (Holm-Bonferroni, Cliff's Delta)
- Certified canonical execution (15.5 hrs, reproduced)
- All datasets RELEASE_RAW (CC-BY-4.0 or Public Domain)
"
git push -u origin main
```

### 5. Create Tag and Release
```bash
git tag -a v1.0.0 -m "HWIN-Bench v1.0.0 — Public Release

Heterogeneous Water Quality Intelligence Benchmark v1.0

Features:
- Frozen, immutable benchmark protocol
- 5 canonical datasets harmonized to CBS
- 51-variable ontology with 89 synonym mappings
- 13 benchmarkable water quality variables (GRQA)
- 7 classical ML models, 5×5 GroupKFold CV
- 2,275 model fits with full statistical testing
- Certified reproducibility

Datasets:
- GRQA v1.4 (CC-BY-4.0) — 25.8M observations, global
- WQP SF Bay (Public Domain) — 51K observations
- STORET CA (Public Domain) — 180K observations
- STORET TX (Public Domain) — 175K observations
- STORET RI (Public Domain) — 2.5K observations

All data RELEASE_RAW with full attribution.
See CHANGELOG.md for complete details.
"
git push origin v1.0.0
```

### 6. GitHub Release UI
- Go to Releases → Create new release
- Tag: `v1.0.0`
- Title: `HWIN-Bench v1.0.0 — Public Release`
- Description: Copy from CHANGELOG.md [1.0.0] section
- Attach: No binaries (data in repo/LFS)
- Publish: **Not a pre-release**

### 7. Zenodo Deposit
```bash
# Deposit the GitHub repository to Zenodo
# 1. Go to zenodo.org → Upload → New upload
# 2. Connect GitHub repository HWIN-Bench/HWIN-Bench-v1.0
# 3. Select tag v1.0.0
# 4. Fill metadata:
#    - Title: "HWIN-Bench v1.0: Heterogeneous Water Quality Intelligence Benchmark"
#    - Authors: HWIN-Bench Consortium
#    - Description: From README.md
#    - License: CC-BY-4.0
#    - Keywords: water quality, benchmark, machine learning, reproducibility
#    - Funding: [add grant numbers]
# 5. Publish → Get DOI
# 6. Update CITATION.cff with Zenodo DOI
# 7. Update README.md with DOI badge
```

---

## Recommended Zenodo Release Contents

For Zenodo (separate from GitHub), deposit:
- **Code + Docs + Ontology + Manifests** (all Git-tracked files)
- **STORET/WQP harmonized data** (small enough for Zenodo)
- **GRQA harmonized data** (may need separate deposit due to 6 GB)
- **Exclude**: Raw GRQA zip files (already on Zenodo at 15335450)

---

## Post-Release Verification

- [ ] Fresh clone works: `git clone https://github.com/HWIN-Bench/HWIN-Bench-v1.0.git`
- [ ] LFS files download: `git lfs pull`
- [ ] Installation works: `conda env create -f environment.yml && pip install -e .`
- [ ] Smoke test passes: `python benchmark/run_full_benchmark_fixed.py --smoke-test`
- [ ] DOI resolves: Check Zenodo DOI
- [ ] Citation.cff valid: `cffconvert --validate`

---

## Contacts

- **Release Engineer**: [name]
- **GitHub Organization Admin**: [name]
- **Zenodo Curator**: [name]

---

**Status**: Ready for execution  
**Version**: 1.0.0  
**Date**: 2026-08-09