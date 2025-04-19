import collections
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        dist = [float('inf')] * n
        dist[start_node] = 1
        Q = [(1, start_node)]
        
        while Q:
            prob, node = heapq.heappop(Q)
            if node == end_node:
                return 1.0 / prob
            for a, b in graph[node]:
                if b != 0 and dist[a] > (prob / b):
                    dist[a] = (prob / b)
                    heapq.heappush(Q, (prob / b, a))
        
        return 0