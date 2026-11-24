"""Ship It Friday — make.fun entry (u-mgwals-ship-it-friday-30bd407a).

Writes the chosen one-line git commit message to entry.txt in the
output directory the grader provides (MAKEFUN_OUTPUT_DIR, default
/output). Deterministic: the same fixed line on every run, no network,
no randomness, no clock reads.
"""

import os

ENTRY = "fix: all 400 tests pass now (I deleted 399) — deploying to prod Friday 4:59pm, see you Monday"

# The gate: entry.txt must be UTF-8 text of 1 to 159 characters, not
# only white space. Fail loudly here rather than shipping an invalid entry.
if not 1 <= len(ENTRY) <= 159 or not ENTRY.strip():
    raise ValueError(f"ENTRY is {len(ENTRY)} chars; gate requires 1-159 non-blank chars")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Write-back verification: what the grader reads must be exactly ENTRY.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise OSError("entry.txt write-back mismatch")
    print(ENTRY)


if __name__ == "__main__":
    main()
