# Last updated: 11/05/2026, 07:07:25
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        total = 0
4
5        for i in range(len(prices)):
6            if (i < len(prices) - 1) and (prices[i + 1] - prices[i] > 0):
7                total += prices[i + 1] - prices[i]
8        
9        return total