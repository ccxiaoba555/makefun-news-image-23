#!/usr/bin/env python3
"""A working news-image-daily entry (Python 3.13, standard library only):
its image is the entry.png beside this file, and the program copies it
to /output/entry.png.

The image is a dense newspaper front page summing up Monday 23 November
2026 in 24 stories, as reported: COP31 collapses with no deal, Iran
strikes Bahrain, a Russian drone flattens a Kyiv apartment block, and
the rest of the day's news. It is 1024x1024 and under 1 MiB, so copying
it is deterministic by construction: two runs write byte-identical files.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    got = os.path.getsize(dst)
    want = os.path.getsize(src)
    if got != want:
        print(f"error: copied {got} bytes, expected {want}", file=sys.stderr)
        return 1
    print(dst, got, "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
