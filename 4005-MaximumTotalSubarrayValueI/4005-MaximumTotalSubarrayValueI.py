# Last updated: 18/08/2026, 14:55:35
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxVal = minVal = nums[0]

        for num in nums:
            maxVal = max(maxVal, num)
            minVal = min(minVal, num)

        return (maxVal - minVal) * k