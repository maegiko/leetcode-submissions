# Last updated: 18/08/2026, 14:55:33
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)

        res = [0] * len(nums)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]
            res[i] = abs(leftSum - rightSum)
            leftSum += nums[i]

        return res

            
        