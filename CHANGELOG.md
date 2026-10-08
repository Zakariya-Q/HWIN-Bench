# Changelog

All notable changes to HWIN-Bench will be documented in this file.

HWIN-Bench **v1.0** is the frozen scientific benchmark/protocol.
Entries below track **repository maintenance releases** (1.0.x) that do not
alter the scientific protocol or canonical results.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - 2026-10-08

Maintenance release. The frozen scientific benchmark (v1.0), its canonical
Run-B point estimates, the 25 recorded fold evaluations, model definitions,
protocol parameters, and source datasets are all unchanged.

### Fixed
- **Canonical Run-B JSON CIs synchronized** with the corrected n=5
  methodology: all 385 metric combinations in
  `benchmark/results/grqa_recomputation/` now report `ci_95` computed from
  the 5 unique GroupKFold folds (n=5, df=4, t=2.7764451051977934) instead of
  the stale n=25 intervals. Point estimates, the 25 recorded fold values,
  and all other statistics are preserved; explicit `n_recorded`,
  `n_unique_folds`, `ci_n`, `ci_df` metadata documents recorded-vs-unique
  counts. Example: VAR-001 extra_trees R²=0.604814 (unchanged), CI
  [0.4979, 0.7117] → [0.2525, 0.9571].
- **Benchmark runner aligned** with the frozen CI methodology: `ci()` is
  replaced by `ci_unique_folds()`, so a fresh full execution reports the same
  n=5 CIs as the canonical artifacts and fails loudly (ValueError) if the
  deterministic-repetition invariant is ever broken. Verified against the
  canonical Run-B fold values (exact reproduction) and the smoke test.
- **CI correction evidence rebuilt from Run B** (`CI_CORRECTION_REVIEW/`):
  the review tables previously carried Run-A-derived figures; they now
  contain the 385 Run-B combinations with two-method verification (direct
  t-formula vs `scipy.stats.t.interval`, max |diff| 9.1e-13 ≤ 1e-12).
- **Checksum verification hardened**: the verifier now LF-normalizes only
  text files — LFS-tracked files and binary suffixes are hashed raw.
  Manifest regenerated under the corrected policy (115 entries), verified
  115/115 locally; Linux CI verifies the same manifest.

No benchmark rerun was required or performed.

## [1.0.3] - 2026-10-08

### Fixed — canonical-run realignment (benchmark-author decision)
- **Canonical run designation**: `grqa_recomputation` (2026-08-06/07, full
  per-fold values) is the canonical v1.0 execution per benchmark-author
  decision. The previously shipped `grqa_full_final_groupkfold` JSONs
  (2026-07-08/09, aggregated means only, different values) removed from
  `benchmark/results/`; both runs' provenance documented in
  BENCHMARK_STATISTICS.md.
- **Confidence intervals recomputed** from the canonical run's stored fold
  values (n=5 unique partitions, df=4, t=2.776). Prior CI figures in summary
  documents matched no stored artifact (width ratio ~1.74 vs the frozen
  3.008 correction ratio) — replaced with values computed directly from data.
- BENCHMARK_STATISTICS.md regenerated; README/docs result tables aligned;
  paper Table5 regenerated; analysis notebook rewritten for the canonical
  schema (executes end-to-end in a clean environment).
- Execution certificates bannered as historical records (R²/best-model
  values canonical; their CI column predates the recomputation).

## [1.0.2] - 2026-10-06

### Repository Hardening (2026-10-08)
- **Installation truthfulness**: HWIN-Bench is a research repository — removed all
  references to the nonexistent `hwin_bench` package, root `requirements.txt`,
  `pip install -e .`, and the broken `hwin-bench @ file:./src` entry in
  `environment.yml`. Conda env is authoritative; pip path points to the real spec.
- **`code/requirements/verify_checksums.py`**: shipped cross-platform SHA-256
  verifier (LF-normalized text, raw LFS) — now the documented verification
  procedure everywhere, replacing incorrect `cd data/ + sha256sum -c` recipes.
- **Canonical execution certificates restored** to `benchmark/reproducibility/`
  (referenced by 9+ documents, directory previously shipped empty).
- **Versioning semantics**: v1.0 = frozen scientific benchmark; 1.0.x = repository
  maintenance. Stated in README, CHANGELOG, CITATION.cff (→ 1.0.2), repo description.
- **CI semantics**: steps labeled `[REQUIRED]` (compile, smoke, checksums — hard
  gates) vs `[INFORMATIONAL]` (CBS validation — documented known findings).
- **Deterministic-repetition clarification**: the canonical seed list produces
  deterministic repetitions of the fixed GroupKFold partition set (5 unique folds);
  documented in the runner docstring and README instead of implying stochastic
  independence.
- **Historical audit docs** (5 files) marked as historical release-audit records,
  superseded for dataset-validation status by
  `docs/DATA_QUALITY_VALIDATION_REPORT.md`.
- **Checksum manifest regenerated** (116 entries) and verified independently.

### Fixed (original v1.0.2 fixes, 2026-10-06)

- **Benchmark runner** (`benchmark/run_full_benchmark_fixed.py`):
  - Removed hardcoded machine-specific input/output paths; data and output
    locations are now CLI arguments (`--data`, `--output-dir`) with
    environment-variable fallbacks (`HWIN_DATA_PATH`, `HWIN_OUTPUT_DIR`,
    `HWIN_VARIABLES`). The runner is now portable across machines.
  - Implemented the `--smoke-test` mode that the README documented but the
    script never had (1 variable, 2 models, 1 seed, 3 folds, subsampled read).
  - Eliminated the duplicate full read of the 6 GB observations CSV
    (auto-selection previously loaded the entire file a second time).
  - Added `--variables` and `--no-auto-select` for explicit variable control.
- **CBS validator** (`code/validation/cbs_validator.py`):
  - The validator crashed (KeyError / timestamp ValueError) on every shipped
    dataset. All checks now guard missing columns and report structured
    errors instead of raising; timestamp parsing uses `errors='coerce'` and
    reports counts. Required columns are split into Tier 1 (core) and
    Tier 2 (CBS-full) with distinct error classes.
  - Full first-run validation results are documented in
    `docs/DATA_QUALITY_VALIDATION_REPORT.md`.
- **STORET timestamps** (RI, CA, TX observations.csv): repaired the
  harmonizer's strftime bug (`T0920:00` → `T09:20:00`, ~383k rows total),
  STORET hour-25 unknown-time sentinels (→ `T00:00:00` + `HOUR25` flag),
  hour-24 end-of-day stamps (→ next-day midnight, instant preserved),
  and corrupt minute values (→ `T00:00:00` + `TIME_CORRUPT`). All repairs
  preserve rows and record provenance in `quality_flag`. Post-repair
  ISO 8601 parseability: RI 2294/2294, CA 172103/172103, TX 210614/210614.
- **dataset.json ×5**: removed invalid null ORCID `0000-0000-0000-0000`,
  removed `[FUNDER NAME TO BE ADDED]` placeholder funding entries, replaced
  placeholder DOIs with the reserved Zenodo DOI 10.5281/zenodo.21877825
  (deposit still unpublished — see `ZENODO_DOI_PENDING.md`).
- **Release integrity**: restored `HWIN-STORET-CA/observations.csv`,
  `HWIN-STORET-TX/observations.csv`, and `HWIN-GRQA-V1-4/stations.json` to
  git tracking (LFS) — they were silently dropped from the tree by the
  v1.0.1-hardening commit while still listed in the release manifests.
  Checksums match the original release manifest.

### Added
- **Canonical benchmark results** (`benchmark/results/grqa_full_final_groupkfold/`):
  the certified 15.5 h run's master JSON + 11 per-variable result files —
  previously referenced by documentation but absent from the repository.
- **CI workflow** (`.github/workflows/ci.yml`): compiles all sources, runs
  CBS validation on shipped datasets, runs the benchmark smoke test on
  in-repo data (no download required), and verifies the checksum manifest.
- **Data quality validation report** (`docs/DATA_QUALITY_VALIDATION_REPORT.md`):
  honest accounting of the CBS findings for each shipped dataset.
- `code/benchmark/__init__.py` (listed in release manifests, was missing).

## [1.0.1] - 2026-08-11

### Fixed
- Documentation, citation, reproducibility, and statistical claims per
  zero-trust audit (see 6998fc1 commit message for the itemized list).

## [1.0.0] - 2026-08-09

### Added
- **Frozen benchmark protocol v1.0** (`benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md`) - immutable scientific contract
- **5 canonical datasets** harmonized to Canonical Benchmark Schema (CBS):
  - HWIN-GRQA-V1-4 (Global River Quality Archive v1.4, CC-BY-4.0)
  - HWIN-WQP-SFBAY (USGS/EPA WQP San Francisco Bay, Public Domain)
  - HWIN-STORET-CA (EPA STORET California, Public Domain)
  - HWIN-STORET-TX (EPA STORET Texas, Public Domain)
  - HWIN-STORET-RI (EPA STORET Rhode Island, Public Domain)
- **Canonical Variable Ontology (CVO v1.0)** - 51 variables (HWIN-VAR-001 to HWIN-VAR-051)
- **Variable Synonym Dictionary** - 89 cross-dataset mappings (Tier 1: 52, Tier 2: 28, Tier 3: 9)
- **Unit Harmonization Rules** - 92 conversion rules to SI units
- **Canonical Benchmark Schema (CBS)** - standardized observation/station/variable format
- **7 classical ML models** with fixed hyperparameters (Linear, Ridge, Lasso, ElasticNet, RF, ExtraTrees, GradientBoosting)
- **5×5 GroupKFold cross-validation** by station_id (2,275 total model fits)
- **5 regression metrics**: MAE, RMSE, R², MAPE, MedAE
- **Statistical testing suite**: Kruskal-Wallis, Wilcoxon, Cliff's Delta, Holm-Bonferroni correction
- **95% confidence intervals** via t-distribution
- **Canonical benchmark runner** (`benchmark/run_full_benchmark_fixed.py`) - single entry point
- **Complete provenance chains** for all 5 datasets (raw → harmonized → benchmark)
- **CBS validation engine** (8 completeness, 38 range, 3 referential integrity, 2 duplicate, 4 temporal, 3 spatial rules)
- **Certified canonical execution** - 15.5 hour run independently reproduced
- **Comprehensive documentation** (QUICKSTART, DATA_GUIDE, DATA_DICTIONARY, REPRODUCIBILITY, LIMITATIONS, DATA_PROVENANCE)
- **License audit** for all 5 datasets with evidence (DATASET_LICENSE_AUDIT.csv)
- **Attribution file** for all source datasets (licenses/ATTRIBUTION.md)
- **GitHub-ready release structure** with Git LFS configuration

### Fixed
- **COMP-006**: Fixed GroupKFold split (was using random split instead of station_id grouping)
- **COMP-005**: Integrated transfer learning evaluation code into canonical repository
- **COMP-003**: Parameterized MIN_SAMPLES according to frozen protocol (100 observations)
- **COMP-004**: Fixed NaN handling in transfer learning evaluation

### Protocol Compliance
- All 74 tests pass
- Protocol frozen - any changes require v1.1 with full re-certification
- Canonical execution command: `python benchmark/run_full_benchmark_fixed.py`
- Expected runtime: ~5-6 hours on CPU (n_jobs=-1 for ensemble models)

### Data Integrity
- All 5 datasets pass CBS validation (Gold/Silver certification)
- SHA256 checksums recorded in dataset manifests
- Row counts, columns, variables, units, station IDs verified against canonical inventory
- No canonical benchmark outputs modified

---

## Pre-Release History

### Release Candidate 1 (RC1) - 2026-07-08
- Initial harmonized datasets deposited to `scripts/archive/output_real_hwin_bench_rc1/`
- GRQA v1.4, WQP-SFBAY, STORET-CA/TX/RI canonicalized
- Validation reports generated
- Dataset manifests with checksums created

### Phase 1: Specification Resolution - 2026-06-28 to 2026-07-03
- Frozen protocol specification completed
- Dataset registry established
- Canonical variable ontology (CVO) v1.0 created
- Variable synonym dictionary (89 mappings) created
- Unit harmonization rules (92 rules) created

### Phase 2: Code Resolution - 2026-07-03 to 2026-07-10
- Canonicalization pipeline implemented (mapper, engine, metadata_aligner, unit_converter)
- Baseline models implemented (7 classical sklearn models)
- Evaluation framework (metrics, statistics, confidence intervals)
- CBS validation engine (58 rules)
- Blocker fixes: COMP-003, COMP-004, COMP-005, COMP-006

### Phase 3: Canonical Execution - 2026-07-10 to 2026-07-24
- Canonical benchmark execution (15.5 hours)
- Reproducibility verification
- Statistical testing with Holm-Bonferroni
- Certification documents generated

### Phase 4: Release Compliance Audit - 2026-08-09
- Dataset license audit (5 datasets)
- Derived data classification audit
- GitHub suitability audit
- Public release package prepared