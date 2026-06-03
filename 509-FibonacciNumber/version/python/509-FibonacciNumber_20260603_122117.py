# Last updated: 03/06/2026, 12:21:17
1class Solution:
2    def fib(self, n: int) -> int:
3        if n == 0:
4            return 0
5        
6        if n == 1:
7            return 1
8        
9        return self.fib(n - 1) + self.fib(n - 2)