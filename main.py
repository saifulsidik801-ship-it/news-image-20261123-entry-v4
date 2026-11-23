#!/usr/bin/env python3
"""Copy the pre-rendered entry.png to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only. Deterministic: the same bytes on every run.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy is incomplete")
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(src)))


if __name__ == "__main__":
    main()
