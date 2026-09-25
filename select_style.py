#!/usr/bin/env python3
"""Print one reusable visual style and its prompt for another skill."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CATALOG = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
parser = argparse.ArgumentParser()
parser.add_argument("style", help="style id such as 08, slug, or a tag")
args = parser.parse_args()
query = args.style.lower()
match = next((item for item in CATALOG["styles"] if item["id"] == query or item["slug"].lower() == query or query in [tag.lower() for tag in item["tags"]]), None)
if not match:
    choices = ", ".join(item["id"] for item in CATALOG["styles"])
    raise SystemExit(f"Unknown style {args.style!r}; choose one of: {choices}")
prompt = (ROOT / match["prompt"]).read_text(encoding="utf-8").strip()
print(json.dumps({"style": match, "prompt": prompt}, ensure_ascii=False, indent=2))
