#!/usr/bin/env python3
"""
update_progress.py
------------------
README.md 내 진행 현황(완료·풀이중·예정) 숫자를 자동 갱신하는 유틸리티.

∙ 문제 디렉터리는  "정수.문제이름"  형태(예: 1.Two_Sum/)라고 가정합니다.
∙ 'solution.py'  파일이 있으면 '완료', 없으면 '풀이 중' 으로 분류합니다.
∙ README.md 에서 `[LeetCode <번호>.` 패턴을 스캔하여 '예정' 개수를 계산합니다.

사용:
    python scripts/update_progress.py
"""
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"

# --------------------------------------------------------------------------- #
# 1. 저장소 상태 분석
# --------------------------------------------------------------------------- #
problem_dirs = [p for p in ROOT.iterdir() if p.is_dir() and re.match(r"^\d+\.", p.name)]
completed = sum((p / "solution.py").exists() for p in problem_dirs)
in_progress = len(problem_dirs) - completed

# README 내 등장하는 모든 문제 번호(정규식 캡처)
readme_text = README_PATH.read_text(encoding="utf-8")
nums_in_readme = set(map(int, re.findall(r"\[LeetCode\s+(\d+)\.", readme_text)))
planned = len(nums_in_readme - {int(re.match(r"^(\d+)\.", p.name).group(1)) for p in problem_dirs})

# --------------------------------------------------------------------------- #
# 2. README.md 숫자 치환
# --------------------------------------------------------------------------- #
def replace_count(label_regex: str, new_value: int, text: str) -> str:
    """
    'label_regex' 로 시작하는 테이블 행에서 **숫자** 값을 new_value 로 교체
    """
    pattern = rf"(\| {label_regex}[^|]*\|\s+\*\*)(\d+)(\*\*)"
    return re.sub(pattern, rf"\g<1>{new_value}\3", text)

updated_text = readme_text
updated_text = replace_count(r"✅", completed, updated_text)
updated_text = replace_count(r"🚧", in_progress, updated_text)
updated_text = replace_count(r"🔜", planned,    updated_text)

# --------------------------------------------------------------------------- #
# 3. 파일 덮어쓰기 (변경이 있을 때만)
# --------------------------------------------------------------------------- #
if updated_text != readme_text:
    README_PATH.write_text(updated_text, encoding="utf-8")
    print(f"[update_progress] README.md 갱신 완료: "
          f"완료={completed}, 진행중={in_progress}, 예정={planned}")
else:
    print("[update_progress] 변경 사항 없음.")

