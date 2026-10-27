#!/usr/bin/env python3
"""Validate Markdown pairs and local links without compiling the site."""

import argparse
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAIRS = {"README.md": "README.zh-CN.md", "CONTRIBUTING.md": "CONTRIBUTING.zh-CN.md"}
PAIRS.update({value: key for key, value in list(PAIRS.items())})


def counterpart(path):
    for source, target in [("en", "zh-CN"), ("zh-CN", "en")]:
        prefix = f"docs/{source}/"
        if path.startswith(prefix) and path.endswith(".md"):
            return f"docs/{target}/{path[len(prefix):]}"
    return PAIRS.get(path)


def check(base=None):
    errors = []
    markdown_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "vendor" not in p.parts]
    for path in markdown_files:
        relative = path.relative_to(ROOT).as_posix()
        paired = counterpart(relative)
        if paired and not (ROOT / paired).is_file():
            errors.append(f"Missing translation: {relative} -> {paired}")
        # Ignore code fences and inline code when inspecting ordinary MD links.
        content = re.sub(r"(?ms)^(`{3,}|~{3,}).*?^\1[^\n]*$", "", path.read_text(encoding="utf-8"))
        content = re.sub(r"`[^`\n]+`", "", content)
        for target in re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", content):
            target = target.strip("<>")
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            dest = unquote(url.path)
            if dest.startswith("/") and relative.startswith("docs/"):
                resolved = ROOT / "docs" / dest.lstrip("/")
            else:
                resolved = path.parent / dest
            if not resolved.exists():
                errors.append(f"Broken link in {relative}: {target}")
    if base and set(base) != {"0"}:
        # --no-renames includes both old and new paths, so paired renames/deletions
        # are checked too. On PRs, use the merge base to compare the actual change.
        result = subprocess.run(
            ["git", "diff", "--no-renames", "--name-only", "-z", f"{base}...HEAD"],
            cwd=ROOT, check=True, capture_output=True,
        )
        changed = set(result.stdout.decode().strip("\0").split("\0"))
        for path in sorted(changed):
            paired = counterpart(path)
            if paired and paired not in changed:
                errors.append(f"Update both languages in the same PR: {path} -> {paired}")
    return errors, len(markdown_files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="Git base commit for paired-change validation")
    args = parser.parse_args()
    errors, count = check(args.base)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print(f"Checked {count} Markdown files: bilingual pairs and local links pass. No build performed.")
