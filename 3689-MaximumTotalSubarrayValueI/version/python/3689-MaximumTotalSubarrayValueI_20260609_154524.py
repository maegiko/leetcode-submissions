# Last updated: 09/06/2026, 15:45:24
1class Solution:
2    def maxTotalValue(self, nums: List[int], k: int) -> int:
3        maxVal = minVal = nums[0]
4
5        for num in nums:
6            maxVal = max(maxVal, num)
7            minVal = min(minVal, num)
8
9        return (maxVal - minVal) * k