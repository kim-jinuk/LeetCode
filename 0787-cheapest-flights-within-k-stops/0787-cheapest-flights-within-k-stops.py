from typing import List

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        dp = [float('inf')] * n
        dp[src] = 0

        # K번 경유 → K+1번 벨만‑포드 반복
        for _ in range(K + 1):
            tmp = dp.copy()
            for u, v, w in flights:
                if dp[u] + w < tmp[v]:
                    tmp[v] = dp[u] + w
            dp = tmp

        return dp[dst] if dp[dst] < float('inf') else -1
