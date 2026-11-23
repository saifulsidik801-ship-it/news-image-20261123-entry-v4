#!/usr/bin/env python3
"""News image 20261123 entry — copy entry.png into the output directory.

Stdlib only. Resolves entry.png from this file's own directory (never the
working directory) and writes it to $MAKEFUN_OUTPUT_DIR (default
<repo>/output), creating the output directory if needed.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    copied = os.path.getsize(dst)
    if copied != os.path.getsize(src):
        raise RuntimeError(
            f"incomplete copy: {dst} is {copied} bytes, expected {os.path.getsize(src)}"
        )
    print(f"copied entry.png to {dst} ({copied} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
