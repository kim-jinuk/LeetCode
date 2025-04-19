import collections, heapq
from typing import List

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        K: int
    ) -> int:
        # 그래프 구성
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # best[도시][경유횟수] = 최소 비용
        best = [[float('inf')] * (K + 2) for _ in range(n)]
        best[src][0] = 0

        pq = [(0, src, 0)]  # (비용, 도시, 사용한 경유 횟수)
        while pq:
            cost, u, stops = heapq.heappop(pq)
            if u == dst:
                return cost
            if stops == K + 1 or cost > best[u][stops]:
                continue
            for v, w in graph[u]:
                nc = cost + w
                # stops+1번 경유해서 v에 올 때 비용이 더 싸면 갱신
                if nc < best[v][stops + 1]:
                    best[v][stops + 1] = nc
                    heapq.heappush(pq, (nc, v, stops + 1))

        return -1
