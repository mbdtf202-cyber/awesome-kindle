#!/usr/bin/env python3
"""Fetch the official KindleModding jailbreaks.json and diff it against our snapshot.

Usage:
  python3 scripts/sync_upstream.py            # fetch, write snapshot, write DIFF.md
Exit codes: 0 ok, 1 network/parse error.
The GitHub workflow reads data/upstream/DIFF.md and opens an issue when non-empty.
"""
import json, sys, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAP = ROOT / "data" / "upstream" / "jailbreaks.json"
DIFF = ROOT / "data" / "upstream" / "DIFF.md"
URL = "https://kindlemodding.org/jailbreaks.json"


def norm(data):
    out = {}
    for m in data:
        fws = []
        for f in m.get("firmwares", []):
            fws.append({
                "models": sorted(f.get("models", [])),
                "min": f.get("min", ""),
                "max": f.get("max", ""),
                "accepted": sorted((f.get("outliers") or {}).get("accepted", [])),
                "denied": sorted((f.get("outliers") or {}).get("denied", [])),
            })
        out[m.get("name", "")] = {
            "models": sorted(m.get("models", [])),
            "registration": bool(m.get("registration")),
            "ads": bool(m.get("ads")),
            "firmwares": fws,
        }
    return out


def main():
    import urllib.request
    try:
        raw = urllib.request.urlopen(URL, timeout=30).read()
        data = json.loads(raw)
    except Exception as e:
        print(f"fetch/parse failed: {e}", file=sys.stderr)
        return 1
    SNAP.parent.mkdir(parents=True, exist_ok=True)
    new = norm(data)
    old = None
    if SNAP.exists():
        try:
            old = norm(json.load(open(SNAP, encoding="utf-8")))
        except Exception:
            old = None
    # write snapshot (raw upstream for provenance)
    SNAP.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if old is None:
        DIFF.write_text("", encoding="utf-8")
        print(f"seeded snapshot: {len(new)} methods")
        return 0

    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = [n for n in sorted(set(new) & set(old)) if new[n] != old[n]]
    if not (added or removed or changed):
        DIFF.write_text("", encoding="utf-8")
        print("no changes")
        return 0

    lines = ["# Upstream compatibility changes", ""]
    if added: lines += ["## Added methods", *[f"- {n}" for n in added], ""]
    if removed: lines += ["## Removed methods", *[f"- {n}" for n in removed], ""]
    if changed:
        lines += ["## Changed methods", ""]
        for n in changed:
            o, c = old[n], new[n]
            if o["models"] != c["models"]:
                lines.append(f"- **{n}**: models changed → {', '.join(c['models'])}")
            if o["firmwares"] != c["firmwares"]:
                om = [f for f in o["firmwares"]]; cm = [f for f in c["firmwares"]]
                lines.append(f"- **{n}**: firmware ranges changed → {json.dumps(cm, ensure_ascii=False)}")
    DIFF.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"CHANGED added={added} removed={removed} changed={changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
