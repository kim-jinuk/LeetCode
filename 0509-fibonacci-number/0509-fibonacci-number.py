class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
            
        a = [0, 1]
        for i in range(2, n + 1):
            a.append(a[i-1] + a[i-2])
        
        return a[-1]