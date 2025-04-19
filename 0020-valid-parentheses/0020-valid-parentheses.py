class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for char in s:
            if char in table:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                open_char = stack.pop()

                if table[open_char] != char:
                    return False
        return not stack