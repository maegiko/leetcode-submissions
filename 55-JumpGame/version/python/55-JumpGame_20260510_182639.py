# Last updated: 10/05/2026, 18:26:39
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        cost = 0
4
5        for i in range(len(nums)):
6            if cost < 0: return False
7
8            if nums[i] > cost:
9                cost = nums[i]
10            
11            cost -= 1
12        
13        return True