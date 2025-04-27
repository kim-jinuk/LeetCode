#!/usr/bin/env python3
"""update_progress.py

Run this script from the repository root. It scans every folder whose name
starts with ``Category_`` (e.g. ``Category_Array``) and treats every
source‑code file inside (`.cpp`, `.py`, `.java`, …) as a solved LeetCode
problem. It then **rewrites** two sections of the top‑level ``README.md``:

1. ``## 유형별 문제 분류`` – a table grouping problems by category
2. ``## 진행 현황``       – overall solved count + per‑category stats

If those headings do not yet exist in README, they are appended at the end.

The sections are delimited by the headings themselves, so everything between
``## 유형별 문제 분류`` and the next heading of the same level will be
automatically replaced.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Dict, List

ALLOWED_EXT = {
    ".py",
    ".cpp",
    ".c",
    ".cc",
    ".cxx",
    ".java",
    ".js",
    ".ts",
    ".go",
    ".rb",
    ".rs",
    ".swift",
}

# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────


def gather_categories(repo_root: Path) -> Dict[str, List[Path]]:
    """Return mapping {category: [file, ...]} for each Category_* folder."""
    categories: Dict[str, List[Path]] = {}
    for item in repo_root.iterdir():
        if item.is_dir() and item.name.startswith("Category_"):
            cat_name = item.name[len("Category_") :]
            # Collect source files recursively
            files = [f for f in item.rglob("*") if f.is_file() and f.suffix.lower() in ALLOWED_EXT]
            categories[cat_name] = sorted(files, key=lambda p: p.name.lower())
    return dict(sorted(categories.items()))  # alphabetical order


def make_md_link(path: Path, repo_root: Path) -> str:
    """Convert a Path to a relative markdown link."""
    rel = path.relative_to(repo_root).as_posix()
    return f"[{path.stem}]({rel})"


def build_category_table(categories: Dict[str, List[Path]], repo_root: Path) -> str:
    """Build markdown table listing all problems in each category."""
    lines: List[str] = ["| 유형 | 문제 수 | 문제 목록 |", "|------|---------|-----------|"]
    for cat, files in categories.items():
        links = "<br>".join(make_md_link(f, repo_root) for f in files) if files else "-"
        lines.append(f"| {cat} | {len(files)} | {links} |")
    return "\n".join(lines)


def build_progress_md(categories: Dict[str, List[Path]], repo_root: Path) -> str:
    total = sum(len(v) for v in categories.values())
    solved_line = f"**Solved:** {total} problems\n"
    return solved_line + "\n" + build_category_table(categories, repo_root) + "\n"


def replace_section(readme: str, heading: str, new_content: str) -> str:
    """Replace the markdown section that starts with *heading* (e.g. '## Title').
    The section goes until the next heading of the same level or EOF."""
    pattern = rf"(^## +{re.escape(heading)}.*?$)([\s\S]*?)(?=^## |\Z)"
    regex = re.compile(pattern, re.MULTILINE)
    if regex.search(readme):
        return regex.sub(rf"\1\n\n{new_content}\n", readme)
    # Heading not found – append to EOF
    return readme.rstrip() + f"\n\n## {heading}\n\n{new_content}\n"


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    readme_path = repo_root / "README.md"

    if not readme_path.exists():
        print("README.md not found in repo root", file=sys.stderr)
        sys.exit(1)

    categories = gather_categories(repo_root)

    with readme_path.open("r", encoding="utf-8") as f:
        readme_text = f.read()

    # Update sections
    readme_text = replace_section(
        readme_text, "유형별 문제 분류", build_category_table(categories, repo_root)
    )
    readme_text = replace_section(
        readme_text, "진행 현황", build_progress_md(categories, repo_root)
    )

    with readme_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(readme_text)

    print("README.md updated successfully.")


if __name__ == "__main__":
    main()
