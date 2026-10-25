#!/usr/bin/env python3
"""Make Polish the first-run language/region defaults without changing user configs.

This script is intentionally idempotent so it can be reapplied after syncing upstream.
"""
from pathlib import Path

path = Path("src/platform/sys.cpp")
source = path.read_text(encoding="utf-8")
pairs = (
    ('    "language = English\\n"', '    "language = Polish\\n"'),
    ('    "sku = EUROPE\\n"', '    "sku = EUROPE\\n"'),
)

for original, desired in pairs:
    if desired in source:
        continue
    count = source.count(original)
    if count != 1:
        raise SystemExit(
            f"Expected exactly one {original!r} in {path}, found {count}; "
            "upstream may have changed the settings template."
        )
    source = source.replace(original, desired, 1)

path.write_text(source, encoding="utf-8")
print("Polish defaults applied: language=Polish, sku=EUROPE")
