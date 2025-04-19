from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = defaultdict(int)
        left, max_length = 0, 0

        if len(s) < 2:
            return len(s)
        
        for i in range(len(s)):
            print(max_length)
            if table[s[i]] == 0:
                table[s[i]] = i + 1
                max_length = max(max_length, i - left + 1)
            else:
                left = max(left, table[s[i]])
                max_length = max(max_length, i - left + 1)
                table[s[i]] = i + 1

        return max_length
        
        