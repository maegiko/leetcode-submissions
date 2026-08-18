# Last updated: 18/08/2026, 14:57:41
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, maxProfit = 0, 0

        for right in range(len(prices)):
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            elif prices[right] < prices[left]:
                left = right
        
        return maxProfit