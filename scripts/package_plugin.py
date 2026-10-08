"""Build checked-in plugin artifacts from the standalone skill sources."""
import argparse
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--check", action="store_true", help="Fail if packaged files differ from sources")
args = parser.parse_args()
manifest = json.loads((root / "plugin/.claude-plugin/plugin.json").read_text())
name = re.search(r"^name: ([a-z0-9-]+)$", (root / "SKILL.md").read_text(), re.M).group(1)
outputs = {}
for source in [root / "SKILL.md", *sorted((root / "references").rglob("*.md"))]:
    outputs[root / "plugin/skills" / name / source.relative_to(root)] = source.read_bytes()
if (root / "LICENSE").exists():
    outputs[root / "plugin/skills" / name / "LICENSE"] = (root / "LICENSE").read_bytes()
metadata = {k: v for k, v in manifest.items() if k != "skills"}
outputs[root / "plugin/.codex-plugin/plugin.json"] = (json.dumps({**metadata, "skills": "./skills/"}, indent=2) + "\n").encode()
outputs[root / "plugin/plugin.json"] = (json.dumps({"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", **metadata}, indent=2) + "\n").encode()
existing = {p for p in (root / "plugin/skills").rglob("*") if p.is_file()}
stale = existing - outputs.keys()
changed = [p for p, content in outputs.items() if not p.exists() or p.read_bytes() != content]
if args.check:
    if stale or changed:
        for p in sorted(stale | set(changed)):
            print(f"Stale package: {p.relative_to(root)}")
        raise SystemExit(1)
    print(f"Package matches source: {manifest['name']} {manifest['version']}")
else:
    for p in stale:
        p.unlink()
    for p, content in outputs.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(content)
    print(f"Packaged {manifest['name']} {manifest['version']}")
