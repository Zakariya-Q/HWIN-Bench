#!/usr/bin/env python3
"""Cross-platform SHA-256 verification for HWIN-Bench.

Verifies data/manifests/checksums.sha256 with correct semantics on any OS:

- Text files: checksums are computed over LF-normalized bytes
  (CRLF -> LF), matching how git stores them. A Windows checkout
  with CRLF endings still verifies.
- LFS-tracked files: checksums are over the raw bytes
  (git never line-ending-normalizes LFS content).

Usage:
    python code/requirements/verify_checksums.py          # from repo root
    python code/requirements/verify_checksums.py --quiet

Exits 0 on full verification, 1 on any mismatch/missing file.
Requires git (for `git lfs ls-files`); without git LFS installed,
all files are treated as text-normalized and LFS files will mismatch
by design — install git-lfs first.
"""
import argparse
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MANIFEST = REPO / "data" / "manifests" / "checksums.sha256"

TEXT_SUFFIXES = {
    ".md", ".txt", ".csv", ".py", ".yml", ".yaml", ".json", ".cff", ".xml",
    ".html", ".css", ".js", ".sh", ".bat", ".ps1", ".rst", ".tex", ".bib",
    ".cfg", ".ini", ".conf", ".toml", ".lock",
}
BINARY_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".zip", ".gz", ".tar",
    ".tgz", ".whl", ".so", ".dll", ".exe", ".pkl", ".npy", ".npz", ".h5",
    ".hdf5", ".parquet", ".feather", ".ipynb", ".docx", ".xlsx", ".pptx",
}


def is_text_file(rel, lfs):
    """Checksum normalization policy (matches .gitattributes intent):
    - LFS-tracked files      -> raw bytes (LFS never normalizes content)
    - known binary suffixes  -> raw bytes
    - known text suffixes    -> LF-normalized bytes
    - unknown suffix         -> LF-normalized bytes (safe default for this
      repository: every non-LFS tracked file with an unknown suffix is a
      text config/source file; if a new binary type is ever added with an
      unlisted suffix, regeneration + this function must be updated together)
    """
    rel = rel.replace("\\", "/")
    if rel in lfs:
        return False
    suffix = Path(rel).suffix.lower()
    if suffix in BINARY_SUFFIXES:
        return False
    return True


def lfs_files():
    if shutil.which("git") is None:
        sys.exit("git not found — install git and git-lfs to verify LFS files")
    out = subprocess.run(
        ["git", "lfs", "ls-files", "--name-only"],
        cwd=REPO, capture_output=True, text=True,
    )
    return {ln.strip().replace("\\", "/") for ln in out.stdout.splitlines() if ln.strip()}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quiet", action="store_true", help="only print failures and summary")
    args = ap.parse_args()

    if not MANIFEST.is_file():
        sys.exit(f"manifest not found: {MANIFEST}")

    lfs = lfs_files()
    ok = bad = missing = 0
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        expected, rel = line.split(None, 1)
        rel = rel.strip().lstrip("*").strip()
        f = REPO / rel
        if not f.is_file():
            print(f"MISSING: {rel}")
            missing += 1
            continue
        raw = f.read_bytes()
        if is_text_file(rel, lfs):
            raw = raw.replace(b"\r\n", b"\n")  # text files: LF-normalized
        actual = hashlib.sha256(raw).hexdigest()
        if actual == expected:
            ok += 1
            if not args.quiet:
                print(f"OK      {rel}")
        else:
            bad += 1
            print(f"MISMATCH {rel}")

    print(f"\nVerification: {ok} OK, {bad} mismatched, {missing} missing "
          f"(LFS files hashed raw: {len(lfs)})")
    sys.exit(1 if (bad or missing) else 0)


if __name__ == "__main__":
    main()
