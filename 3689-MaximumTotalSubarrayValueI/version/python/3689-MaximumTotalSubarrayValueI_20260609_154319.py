# Last updated: 09/06/2026, 15:43:19
1class Solution:
2    def maxTotalValue(self, nums: List[int], k: int) -> int:
3        maxVal = 0
4        minVal = float("inf")
5
6        for num in nums:
7            maxVal = max(maxVal, num)
8            minVal = min(minVal, num)
9        
10        diff = maxVal - minVal
11
12        return diff * k