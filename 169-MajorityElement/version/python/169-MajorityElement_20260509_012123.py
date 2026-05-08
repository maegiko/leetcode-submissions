# Last updated: 09/05/2026, 01:21:23
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        numbers = nums.sort()
4
5        middle = (len(nums) // 2)
6
7        return nums[middle]