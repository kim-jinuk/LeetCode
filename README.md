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

## 유형별 문제 분류

| 유형 | 문제 수 | 문제 목록 |
|------|---------|-----------|
| DP | 6 | [0053-maximum-subarray](Category_DP/0053-maximum-subarray/0053-maximum-subarray.py)<br>[0070-climbing-stairs](Category_DP/0070-climbing-stairs/0070-climbing-stairs.py)<br>[0198-house-robber](Category_DP/0198-house-robber/0198-house-robber.py)<br>[0509-fibonacci-number](Category_DP/0509-fibonacci-number/0509-fibonacci-number.py)<br>[test](Category_DP/zero-one-knapsack-problem/test.py)<br>[zero-one-knapsack-problem](Category_DP/zero-one-knapsack-problem/zero-one-knapsack-problem.py) |
| array | 1 | [0056-merge-intervals](Category_array/0056-merge-intervals/0056-merge-intervals.py) |
| divide_conquer | 2 | [0169-majority-element](Category_divide_conquer/0169-majority-element/0169-majority-element.py)<br>[0241-different-ways-to-add-parentheses](Category_divide_conquer/0241-different-ways-to-add-parentheses/0241-different-ways-to-add-parentheses.py) |
| etc | 1 | [0042-trapping-rain-water](Category_etc/0042-trapping-rain-water/0042-trapping-rain-water.py) |
| graph | 4 | [0743-network-delay-time](Category_graph/0743-network-delay-time/0743-network-delay-time.py)<br>[0787-cheapest-flights-within-k-stops](Category_graph/0787-cheapest-flights-within-k-stops/0787-cheapest-flights-within-k-stops.py)<br>[1514-path-with-maximum-probability](Category_graph/1514-path-with-maximum-probability/1514-path-with-maximum-probability.py)<br>[1631-path-with-minimum-effort](Category_graph/1631-path-with-minimum-effort/1631-path-with-minimum-effort.py) |
| greedy | 5 | [0122-best-time-to-buy-and-sell-stock-ii](Category_greedy/0122-best-time-to-buy-and-sell-stock-ii/0122-best-time-to-buy-and-sell-stock-ii.py)<br>[0134-gas-station](Category_greedy/0134-gas-station/0134-gas-station.py)<br>[0406-queue-reconstruction-by-height](Category_greedy/0406-queue-reconstruction-by-height/0406-queue-reconstruction-by-height.py)<br>[0455-assign-cookies](Category_greedy/0455-assign-cookies/0455-assign-cookies.py)<br>[0621-task-scheduler](Category_greedy/0621-task-scheduler/0621-task-scheduler.py) |
| hash_table | 1 | [0017-letter-combinations-of-a-phone-number](Category_hash_table/0017-letter-combinations-of-a-phone-number/0017-letter-combinations-of-a-phone-number.py) |
| linked_list | 1 | [0148-sort-list](Category_linked_list/0148-sort-list/0148-sort-list.py) |
| stack_queue | 1 | [0020-valid-parentheses](Category_stack_queue/0020-valid-parentheses/0020-valid-parentheses.py) |
| string | 1 | [0003-longest-substring-without-repeating-characters](Category_string/0003-longest-substring-without-repeating-characters/0003-longest-substring-without-repeating-characters.py) |
| tree | 0 | - |

## 진행 현황

**Solved:** 23 problems

| 유형 | 문제 수 | 문제 목록 |
|------|---------|-----------|
| DP | 6 | [0053-maximum-subarray](Category_DP/0053-maximum-subarray/0053-maximum-subarray.py)<br>[0070-climbing-stairs](Category_DP/0070-climbing-stairs/0070-climbing-stairs.py)<br>[0198-house-robber](Category_DP/0198-house-robber/0198-house-robber.py)<br>[0509-fibonacci-number](Category_DP/0509-fibonacci-number/0509-fibonacci-number.py)<br>[test](Category_DP/zero-one-knapsack-problem/test.py)<br>[zero-one-knapsack-problem](Category_DP/zero-one-knapsack-problem/zero-one-knapsack-problem.py) |
| array | 1 | [0056-merge-intervals](Category_array/0056-merge-intervals/0056-merge-intervals.py) |
| divide_conquer | 2 | [0169-majority-element](Category_divide_conquer/0169-majority-element/0169-majority-element.py)<br>[0241-different-ways-to-add-parentheses](Category_divide_conquer/0241-different-ways-to-add-parentheses/0241-different-ways-to-add-parentheses.py) |
| etc | 1 | [0042-trapping-rain-water](Category_etc/0042-trapping-rain-water/0042-trapping-rain-water.py) |
| graph | 4 | [0743-network-delay-time](Category_graph/0743-network-delay-time/0743-network-delay-time.py)<br>[0787-cheapest-flights-within-k-stops](Category_graph/0787-cheapest-flights-within-k-stops/0787-cheapest-flights-within-k-stops.py)<br>[1514-path-with-maximum-probability](Category_graph/1514-path-with-maximum-probability/1514-path-with-maximum-probability.py)<br>[1631-path-with-minimum-effort](Category_graph/1631-path-with-minimum-effort/1631-path-with-minimum-effort.py) |
| greedy | 5 | [0122-best-time-to-buy-and-sell-stock-ii](Category_greedy/0122-best-time-to-buy-and-sell-stock-ii/0122-best-time-to-buy-and-sell-stock-ii.py)<br>[0134-gas-station](Category_greedy/0134-gas-station/0134-gas-station.py)<br>[0406-queue-reconstruction-by-height](Category_greedy/0406-queue-reconstruction-by-height/0406-queue-reconstruction-by-height.py)<br>[0455-assign-cookies](Category_greedy/0455-assign-cookies/0455-assign-cookies.py)<br>[0621-task-scheduler](Category_greedy/0621-task-scheduler/0621-task-scheduler.py) |
| hash_table | 1 | [0017-letter-combinations-of-a-phone-number](Category_hash_table/0017-letter-combinations-of-a-phone-number/0017-letter-combinations-of-a-phone-number.py) |
| linked_list | 1 | [0148-sort-list](Category_linked_list/0148-sort-list/0148-sort-list.py) |
| stack_queue | 1 | [0020-valid-parentheses](Category_stack_queue/0020-valid-parentheses/0020-valid-parentheses.py) |
| string | 1 | [0003-longest-substring-without-repeating-characters](Category_string/0003-longest-substring-without-repeating-characters/0003-longest-substring-without-repeating-characters.py) |
| tree | 0 | - |

