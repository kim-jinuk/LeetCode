import collections

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, column = len(heights), len(heights[0])
        Q = [(0, 0, 0)]
        effort = collections.defaultdict(int)
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while 1:
            e, x, y = heapq.heappop(Q)
            if x == row - 1 and y == column - 1:
                return e
            if (x, y) not in effort:
                effort[(x, y)] = e
                for dx, dy in move:
                    if 0 <= x + dx < row and 0 <= y + dy < column:
                        value = max(heights[x + dx][y + dy] - heights[x][y], heights[x][y] - heights[x + dx][y + dy])
                        heapq.heappush(Q, (max(e, value), x + dx, y + dy))
        
        return Q[0][0]