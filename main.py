"""mdev-1125 entry builder: ships the one-line excuse to the makefun output dir."""

import json
import os
import sys

LO, HI = 1, 200


def load_line():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as fh:
        return fh.read().strip()


def ship(line):
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(os.path.abspath(__file__))
    if not os.path.isdir(base):
        os.makedirs(base)
    dst = os.path.join(base, "entry.txt")
    with open(dst, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    return dst


line = load_line()
if len(line) < LO or len(line) > HI:
    sys.exit("gate: %d chars outside %d..%d" % (len(line), LO, HI))
dst = ship(line)
print(json.dumps({"status": "shipped", "len": len(line), "words": len(line.split()), "dst": dst, "head": line[:48]}))
