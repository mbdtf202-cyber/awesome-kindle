# data / resources.json

A **machine-readable index** of every resource listed in the README — handy for building
sites, search tools, or integrations.

- **File:** `resources.json`
- **Count:** 118 items (12 jailbreak methods + 106 tools/sites)
- **Source:** auto-generated from the tables in [`README_EN.md`](../README_EN.md)
- **Generator:** [`scripts/build_resources.py`](../scripts/build_resources.py)

## Schema

```json
{
  "repo": "awesome-kindle",
  "generated": "2026-11-12",
  "source": "README_EN.md",
  "count": 118,
  "items": [
    {
      "name": "KOReader",
      "url": "https://github.com/koreader/koreader",
      "links": ["https://github.com/koreader/koreader"],
      "description": "Cross-platform open-source reader — the top pick after jailbreaking.",
      "section": "📚 Reading & library tools",
      "subsection": null,
      "kind": "resource"
    }
  ]
}
```

| Field | Meaning |
| --- | --- |
| `name` | Display name |
| `url` | Primary link |
| `links` | All links found in the row (primary first) |
| `description` | One-line description |
| `section` | Top-level README section (category) |
| `subsection` | Sub-section, if any |
| `kind` | `"jailbreak"` or `"resource"` |

## Regenerate

```bash
python3 scripts/build_resources.py
```

This writes both `data/resources.json` and a copy at `docs/resources.json` for the static site.
**Do not edit the JSON by hand** — edit the README tables, then regenerate.
