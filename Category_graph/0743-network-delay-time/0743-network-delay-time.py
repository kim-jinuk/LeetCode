import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, c in times:
            graph[a].append((b, c))
        
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for b, c in graph[node]:
                    heapq.heappush(Q, (time + c, b))
        
        if len(dist) == n:
            return max(dist.values())
        return -1