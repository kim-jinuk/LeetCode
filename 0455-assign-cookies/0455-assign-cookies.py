from collections import deque

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0

        result = 0
        g.sort()
        s = deque(sorted(s))

        for i in g:
            if not s or i > max(s):
                return result

            while (i > s[0]):
                s.popleft()
            result += 1
            s.popleft()

        return result