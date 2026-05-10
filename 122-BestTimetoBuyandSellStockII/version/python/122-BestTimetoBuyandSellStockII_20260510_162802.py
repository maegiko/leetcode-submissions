# Last updated: 10/05/2026, 16:28:02
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        total = 0
4
5        for i in range(len(prices)):
6            if i < len(prices) - 1:
7                diff = prices[i + 1] - prices[i]
8                if diff >= 0:
9                    total += diff
10        
11        return total
12