#!/usr/bin/env python3
"""update_progress.py

Usage:  python script/update_progress.py

* Scans every directory whose name starts with ``Category_`` and treats any
  source-code file therein (``.cpp``, ``.py``, etc.) as a **solved LeetCode
  problem**.
* Rewrites **in‑place** the two designated sections of the top‑level
  ``README.md`` _only_ if the headings already exist:

    ## 📂 유형별 문제 분류
    ## 🧠 진행 현황

  If either heading is missing, the script aborts with an error instead of
  silently appending content elsewhere. This guarantees the README layout
  remains stable and predictable.
"""
from __future__ import annotations

import sys
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# ────────────────────────────────────────────────
# Settings
# ────────────────────────────────────────────────

ALLOWED_EXT = {
    ".py", ".cpp", ".c", ".cc", ".cxx", ".java", ".js", ".ts", ".go", ".rb", ".rs", ".swift"
}

HEAD_CATEGORIES = "📂 유형별 문제 분류"
HEAD_PROGRESS = "🧠 진행 현황"

# ────────────────────────────────────────────────
# Helpers
# ────────────────────────────────────────────────

def gather_categories(repo_root: Path) -> Dict[str, List[Path]]:
    """Return {category_name: [files]} sorted alphabetically."""
    cats: Dict[str, List[Path]] = {}
    for p in repo_root.iterdir():
        if p.is_dir() and p.name.startswith("Category_"):
            name = p.name[len("Category_"):]
            files = [f for f in p.rglob("*") if f.is_file() and f.suffix.lower() in ALLOWED_EXT]
            cats[name] = sorted(files, key=lambda x: x.name.lower())
    return dict(sorted(cats.items()))


def md_link(file: Path, repo_root: Path) -> str:
    rel = file.relative_to(repo_root).as_posix()
    return f"[{file.stem}]({rel})"


def build_category_table(cats: Dict[str, List[Path]], repo_root: Path) -> str:
    lines = [
        "| 유형 | 문제 수 | 문제 목록 |",
        "|------|---------|-----------|",
    ]
    for cat, files in cats.items():
        links = "<br>".join(md_link(f, repo_root) for f in files) if files else "-"
        lines.append(f"| {cat} | {len(files)} | {links} |")
    return "\n".join(lines)


def build_progress_block(cats: Dict[str, List[Path]]) -> str:
    total = sum(len(v) for v in cats.values())
    per_cat = ", ".join(f"{k}: {len(v)}" for k, v in cats.items())
    return (
        f"현재까지 **{total}개** 문제 해결\n\n"
        f"분류별 현황: {per_cat if per_cat else 'N/A'}\n"
    )


def replace_section(readme_text: str, heading: str, new_body: str) -> str:
    """Replace the markdown heading section _in‑place_. Error if not found."""
    pattern = rf"(^## +{re.escape(heading)}.*?$)([\s\S]*?)(?=^## |\Z)"
    regex = re.compile(pattern, re.MULTILINE)
    match = regex.search(readme_text)
    if not match:
        sys.exit(f"[ERROR] Heading '## {heading}' not found in README.md")
    start = match.group(1)
    return regex.sub(f"{start}\n\n{new_body}\n", readme_text)

# ────────────────────────────────────────────────
# Main
# ────────────────────────────────────────────────

def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    readme = repo_root / "README.md"

    if not readme.exists():
        sys.exit("[ERROR] README.md not found at repository root.")

    cats = gather_categories(repo_root)

    with readme.open("r", encoding="utf-8") as fp:
        text = fp.read()

    text = replace_section(text, HEAD_CATEGORIES, build_category_table(cats, repo_root))
    text = replace_section(text, HEAD_PROGRESS, build_progress_block(cats))

    with readme.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)

    print("README.md successfully updated ✅")


if __name__ == "__main__":
    main()
