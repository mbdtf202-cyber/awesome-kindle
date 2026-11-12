#!/usr/bin/env python3
"""Validate the generated data files (stdlib only). Fails loudly on inconsistencies."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

def check(cond, msg):
    if not cond:
        errors.append(msg)

res = json.load(open(ROOT / "data" / "resources.json", encoding="utf-8"))
check(isinstance(res.get("items"), list), "resources.json: items must be a list")
check(res.get("count") == len(res.get("items", [])), "resources.json: count != len(items)")
for i, it in enumerate(res.get("items", [])):
    check(it.get("name"), f"item[{i}] missing name")
    check(str(it.get("url", "")).startswith("http"), f"item[{i}] bad url: {it.get('url')}")
    check(it.get("kind") in ("jailbreak", "resource"), f"item[{i}] bad kind: {it.get('kind')}")
    check(isinstance(it.get("links"), list) and it["links"], f"item[{i}] missing links")

site = ROOT / "docs" / "resources.json"
if site.exists():
    check(json.load(open(site, encoding="utf-8")) == res, "docs/resources.json is out of sync with data/resources.json")

jb = json.load(open(ROOT / "data" / "jailbreaks.json", encoding="utf-8"))
check(len(jb) >= 10, "jailbreaks.json looks too small")
for m in jb:
    check(m.get("name") and m.get("firmware") is not None, "jailbreaks.json: method missing fields")

if errors:
    print("VALIDATION FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print(f"OK: {res['count']} resources, {len(jb)} jailbreak methods")
