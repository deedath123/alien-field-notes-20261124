"""Alien Field Notes: The Two Day Earth Review — round-1 probe.

Writes one alien tourist's one-line review of Earth to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Stdlib only, deterministic.

Entry (187 chars, 187 bytes, one line, no trailing newline):
  Earth, 3/5 stars. Stunning oceans, but the locals stare at glowing
  rectangles 7 hours a day, ignore the microwave beep, reheat the same
  meal twice, and call it dinner. Would abduct again.

End-to-end check: verified by running — /output/entry.txt is UTF-8,
187 characters, 187 bytes, one line, no trailing newline, not
whitespace-only. Re-runs into fresh output dirs and a clean-env run
(env -i python3 -P -s main.py) produce byte-identical output (cmp clean).
"""

import os
import sys

ENTRY = (
    "Earth, 3/5 stars. Stunning oceans, but the locals stare at glowing "
    "rectangles 7 hours a day, ignore the microwave beep, reheat the same "
    "meal twice, and call it dinner. Would abduct again."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be whitespace-only"
    assert "\n" not in ENTRY, "entry must be a single line"
    with open(path, "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
