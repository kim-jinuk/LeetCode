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

- [LeetCode 1. Two Sum](./1.Two_Sum/)
- [LeetCode 121. Best Time to Buy and Sell Stock](./121.Best_Time_to_Buy_and_Sell_Stock/)
- [LeetCode 561. Array Partition I](./561.Array_Partition_I/)

</details>

<details>
<summary>📌 문자열 (String)</summary>

- [LeetCode 5. Longest Palindromic Substring](./5.Longest_Palindromic_Substring/)
- [LeetCode 49. Group Anagrams](./49.Group_Anagrams/)
- [LeetCode 937. Reorder Data in Log Files](./937.Reorder_Data_in_Log_Files/)

</details>

<details>
<summary>📌 연결 리스트 (Linked List)</summary>

- [LeetCode 2. Add Two Numbers](./2.Add_Two_Numbers/)
- [LeetCode 206. Reverse Linked List](./206.Reverse_Linked_List/)
- [LeetCode 21. Merge Two Sorted Lists](./21.Merge_Two_Sorted_Lists/)

</details>

<details>
<summary>📌 스택/큐 (Stack / Queue)</summary>

- [LeetCode 20. Valid Parentheses](./20.Valid_Parentheses/)
- [LeetCode 739. Daily Temperatures](./739.Daily_Temperatures/)
- [LeetCode 225. Implement Stack using Queues](./225.Implement_Stack_using_Queues/)

</details>

<details>
<summary>📌 해시 테이블 (Hash Table)</summary>

- [LeetCode 387. First Unique Character in a String](./387.First_Unique_Character_in_a_String/)
- [LeetCode 146. LRU Cache](./146.LRU_Cache/)
- [LeetCode 819. Most Common Word](./819.Most_Common_Word/)

</details>

<details>
<summary>📌 이진 트리 (Binary Tree)</summary>

- [LeetCode 104. Maximum Depth of Binary Tree](./104.Maximum_Depth_of_Binary_Tree/)
- [LeetCode 226. Invert Binary Tree](./226.Invert_Binary_Tree/)
- [LeetCode 617. Merge Two Binary Trees](./617.Merge_Two_Binary_Trees/)

</details>

<details>
<summary>📌 그래프 & BFS/DFS (Graph)</summary>

- [LeetCode 200. Number of Islands](./200.Number_of_Islands/)
- [LeetCode 207. Course Schedule](./207.Course_Schedule/)
- [LeetCode 433. Minimum Genetic Mutation](./433.Minimum_Genetic_Mutation/)

</details>

<details>
<summary>📌 다이나믹 프로그래밍 (Dynamic Programming)</summary>

- [LeetCode 70. Climbing Stairs](./70.Climbing_Stairs/)
- [LeetCode 198. House Robber](./198.House_Robber/)
- [LeetCode 322. Coin Change](./322.Coin_Change/)

</details>

<details>
<summary>📌 기타 (Bit, Heap, Greedy…)</summary>

- [LeetCode 191. Number of 1 Bits](./191.Number_of_1_Bits/)
- [LeetCode 215. Kth Largest Element in an Array](./215.Kth_Largest_Element_in_an_Array/)
- [LeetCode 621. Task Scheduler](./621.Task_Scheduler/)

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
├── 1.Two_Sum/
│   ├── solution.py
│   ├── README.md
│   └── test.py
├── 2.Add_Two_Numbers/
│   ├── solution.py
│   └── README.md
├── 70.Climbing_Stairs/
│   ├── solution.py
│   └── README.md
├── 104.Maximum_Depth_of_Binary_Tree/
│   ├── solution.py
│   └── README.md
├── scripts/
│   └── update_progress.py
└── README.md

