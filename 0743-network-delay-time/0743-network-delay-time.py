from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, c in times:
            graph[a].append((b, c))
        
        dist = defaultdict(int)
        queue = [(0, k)]

        while queue:
            time, node = heapq.heappop(queue)
            if node not in dist:
                dist[node] = time
                for i, j in graph[node]:
                    heapq.heappush(queue, (time + j, i))
        
        if (len(dist)) == n:
            return max(dist.values())
        return -1