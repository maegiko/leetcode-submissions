# Last updated: 09/05/2026, 18:06:58
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        left, maxProfit = 0, 0
4
5        for right in range(len(prices)):
6            if prices[right] > prices[left]:
7                maxProfit = max(maxProfit, prices[right] - prices[left])
8            elif prices[right] < prices[left]:
9                left = right
10        
11        return maxProfit