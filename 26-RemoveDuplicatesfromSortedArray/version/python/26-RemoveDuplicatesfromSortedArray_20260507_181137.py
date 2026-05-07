# Last updated: 07/05/2026, 18:11:37
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        k = 0
4        seen = set()
5
6        for i in range(len(nums)):
7            if nums[i] not in seen:
8                nums[k] = nums[i]
9                k += 1
10                seen.add(nums[i])
11        
12        return k