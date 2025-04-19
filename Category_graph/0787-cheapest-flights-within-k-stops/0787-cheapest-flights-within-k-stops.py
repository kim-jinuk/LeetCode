import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, c in flights:
            graph[a].append((b, c))

        best = [[float('inf')] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        Q = [(0, src, 0)]
        while Q:
            p, s, cnt = heapq.heappop(Q)
            if s == dst:
                return p
            if cnt == k + 1 or best[s][cnt] < p:
                continue
            for a, b in graph[s]:
                nx = p + b
                if best[a][cnt + 1] > nx:
                    best[a][cnt + 1] = nx
                    heapq.heappush(Q, (nx, a, cnt + 1))

        return -1
                