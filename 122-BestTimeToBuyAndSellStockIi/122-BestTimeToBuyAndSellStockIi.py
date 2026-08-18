# Last updated: 18/08/2026, 14:57:30
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0

        for i in range(len(prices)):
            if (i < len(prices) - 1) and (prices[i + 1] - prices[i] > 0):
                total += prices[i + 1] - prices[i]
        
        return total