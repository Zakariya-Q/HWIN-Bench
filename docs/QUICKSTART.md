# Quickstart — HWIN-Bench v1.0

This guide separates the no-download smoke test from the full canonical benchmark. The full run requires the harmonized GRQA observation payload from GitHub Release v1.0.4; it is not included as a normal file in the repository tree.

## Requirements

- Python 3.11 or later
- Git and Git LFS installed
- For the full benchmark, 32 GB RAM is recommended; the certified run used an 8-core CPU and 32 GB RAM. A 16 GB machine may run out of memory with the current in-memory data-loading path.
- Enough free storage for the 6.02 GB GRQA observations CSV, intermediate files and results; reserve at least 15 GB.
- GitHub CLI (`gh`) for downloading release assets, plus a Bash-compatible shell (Linux, macOS, WSL, or Git Bash).

## 1. Clone and install

~~~bash
git clone https://github.com/Zakariya-Q/HWIN-Bench.git
cd HWIN-Bench
conda env create -f environment.yml
conda activate hwin-bench
~~~

Alternatively, install dependencies with `pip install -r code/requirements/requirements.txt` in a suitable Python environment.

## 2. Verify checked-in files

With Git LFS installed and its objects materialized, run this from the repository root:

~~~bash
python code/requirements/verify_checksums.py
~~~

## 3. Run the smoke test (no GRQA download required)

~~~bash
python benchmark/run_full_benchmark_fixed.py \
  --data data/harmonized/HWIN-STORET-RI/observations.csv \
  --output-dir output/smoke_results \
  --smoke-test
~~~

This is a short execution check, not a data-quality certification. STORET-RI has known strict-CBS validation findings; see `docs/DATA_QUALITY_VALIDATION_REPORT.md`.

## 4. Download and restore GRQA observations

~~~bash
mkdir -p hwin-grqa-release
gh release download v1.0.4 --repo Zakariya-Q/HWIN-Bench \
  --pattern 'hwin-grqa-v1-4_observations.csv.gz.part-*' --dir hwin-grqa-release
cat hwin-grqa-release/hwin-grqa-v1-4_observations.csv.gz.part-* | gzip -t
cat hwin-grqa-release/hwin-grqa-v1-4_observations.csv.gz.part-* | gzip -dc > data/harmonized/HWIN-GRQA-V1-4/observations.csv
sha256sum data/harmonized/HWIN-GRQA-V1-4/observations.csv
~~~

Expected SHA-256: `989e5a6ba07499d81443c8819ef7f1e786fdef8a52661474a2bf5cc4a2ed6f8f`; expected size 6,016,295,802 bytes and 25,850,907 observation rows (25,850,908 lines including the header). See `docs/DATA_AVAILABILITY.md` for release asset details.

## 5. Full benchmark execution

Run from the repository root with a clean output directory:

~~~bash
python benchmark/run_full_benchmark_fixed.py \
  --data data/harmonized/HWIN-GRQA-V1-4/observations.csv \
  --output-dir output/benchmark_results/grqa_recomputation
~~~

The certified canonical execution recorded approximately **15.5 hours (932.4 minutes) wall-clock** on an 8-core CPU with 32 GB RAM. This is total execution time; the approximately 8.8-hour aggregate model-training time reported elsewhere is a component of the total, not additional time. Actual runtime depends on hardware and software.

### Important scientific-scope note

The frozen v1.0 protocol document currently states a 13-variable scope, while the released canonical result artifacts contain 11 variables. This discrepancy is unresolved. This documentation update does not modify the frozen protocol, model results, or claim complete protocol compliance. Resolve the scope through a formally versioned protocol decision and, if needed, a new run before making a final ESSD reproducibility claim.

## 6. Reference results

Current historical canonical result artifacts are under `benchmark/results/grqa_recomputation/`. They are not a substitute for documenting the protocol-scope discrepancy. Corrected confidence intervals use five unique GroupKFold partitions (`n=5`, `df=4`) because five recorded seed repetitions recreate the same deterministic partitions.

## Troubleshooting

| Problem | Action |
|---|---|
| GRQA observations file missing | Download all ten observation parts from GitHub Release v1.0.4 and reassemble as above. |
| Checksum mismatch | Confirm every part was downloaded, concatenated in filename order, and decompressed with gzip; compare against the canonical hash. |
| Memory failure | Use a machine with more RAM or optimize the runner's memory-loading path before a full run. Do not change protocol parameters silently. |
| Regional validation failure | Consult `docs/DATA_QUALITY_VALIDATION_REPORT.md`; smoke-test completion does not imply strict CBS compliance. |
| Runtime estimate | Use 15.5 hours as the recorded canonical wall-clock reference, not 5–6 hours. |

## Further reading

- `docs/DATA_AVAILABILITY.md`
- `docs/DATA_GUIDE.md`
- `docs/REPRODUCIBILITY.md`
- `docs/DATA_QUALITY_VALIDATION_REPORT.md`
- `docs/LIMITATIONS.md`
- `benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md` (frozen protocol; do not edit as part of documentation maintenance)
