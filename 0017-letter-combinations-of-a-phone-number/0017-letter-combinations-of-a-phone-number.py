from collections import defaultdict, deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        converted_letter = {
            2: ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'], 5: ['j','k','l'],
            6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y','z']
        }
        answer = []
        
        def dfs(digit, words):
            if len(words) == len(digits):
                answer.append(words)
                return
            for j in converted_letter[int(digit[0])]:
                words += j
                dfs(digit[1:], words)
                words = words[:-1]

        dfs(digits, "")
        return answer