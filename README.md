# 📘 Python 알고리즘 인터뷰 × LeetCode 풀이집

[![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Last Commit](https://img.shields.io/github/last-commit/<YOUR_ID>/<REPO_NAME>.svg)](https://github.com/<YOUR_ID>/<REPO_NAME>/commits/main)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> **목표**  
> 이 레포는 "파이썬 알고리즘 인터뷰" 교재의 문제들을 LeetCode에서 풀고, 각 문제에 대한 풀이 코드 + 해설 정리를 유형별로 분류한 저장소입니다.  
> 주요 언어: Python3  
> 참고 서적: 파이썬 알고리즘 인터뷰 (저자: 박상길)  

---

## 📑 Table of Contents
1. [유형별 문제 분류](#-유형별-문제-분류)
2. [진행 현황](#-진행-현황)
3. [디렉토리 구조](#-디렉토리-구조)

---

## 📂 유형별 문제 분류

<details>
<summary>📌 배열 (Array)</summary>

- [LeetCode 56. merge intervals](./Category_array/0056-merge-intervals/)

</details>

<details>
<summary>📌 문자열 (String)</summary>



</details>

<details>
<summary>📌 연결 리스트 (Linked List)</summary>

- [LeetCode 148. sort list](./Category_linked_list/0148-sort-list/)

</details>

<details>
<summary>📌 스택/큐 (Stack / Queue)</summary>



</details>

<details>
<summary>📌 해시 테이블 (Hash Table)</summary>



</details>

<details>
<summary>📌 트리 (Tree)</summary>



</details>

<details>
<summary>📌 그래프 & BFS/DFS (Graph)</summary>

- [LeetCode 0743. network delay time](./Category_graph/0743-network-delay-time/)
- [LeetCode 0787. cheapest flights within k stops](./Category_graph/0787-cheapest-flights-within-k-stops/)
- [LeetCode 1514. path with maximum probability](./Category_graph/1514-path-with-maximum-probability/)
- [LeetCode 1631. path with minimum effort](./Category_graph/1631-path-with-minimum-effort/)

</details>

<details>
<summary>📌 그리디 알고리즘</summary>



</details>

<details>
<summary>📌 분할 정복</summary>



</details>

<details>
<summary>📌 다이나믹 프로그래밍 (Dynamic Programming)</summary>



</details>

<details>
<summary>📌 기타 (Binary search, Sliding window, Heap, …)</summary>



</details>

---

## 🧠 진행 현황
| 구분 | 문제 수 |
|------|---------|
| ✅ 완료 | **20** |
| 🚧 풀이 중 | **5** |
| 🔜 예정 | **10** |

> 자동 업데이트 스크립트(`scripts/update_progress.py`)를 통해 커밋 시 README 내 숫자를 갱신할 수 있습니다.

---

## 🗂️ 디렉토리 구조
```bash
.
├── Category_array/
│   └── 0056-merge-intervals
│       ├── solution.py
│       └── README.md
├── Category_graph/
│   ├── 0743-network-delay-time
│   │   ├── solution.py
│   │   └── README.md
│   ├── 0787-cheapest-flights-within-k-stops
│   │   ├── solution.py
│   │   └── README.md
│   └── 0787-cheapest-flights-within-k-stops
│       ├── solution.py
│       └── README.md
├── Category_linked_list/
│   └── 0148-sort-list
│       ├── solution.py
│       └── README.md
├── scripts/
│   └── update_progress.py
└── README.md

