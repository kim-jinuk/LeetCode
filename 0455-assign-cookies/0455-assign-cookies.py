from collections import deque

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0

        result = 0
        g.sort()
        s = deque(sorted(s))

        for i in g:
            if not s:
                return result
            if i <= s[0]:
                result += 1
                s.popleft()
            else:
                while (g[0] > s[0]):
                    s.popleft()
        
        return result