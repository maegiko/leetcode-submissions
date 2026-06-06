# Last updated: 06/06/2026, 14:53:47
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        total = sum(nums)
4
5        res = [0] * len(nums)
6
7        leftSum = 0
8        for i in range(len(nums)):
9            rightSum = total - leftSum - nums[i]
10            res[i] = abs(leftSum - rightSum)
11            leftSum += nums[i]
12
13        return res
14
15            
16        