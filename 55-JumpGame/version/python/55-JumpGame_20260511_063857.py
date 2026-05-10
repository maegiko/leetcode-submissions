# Last updated: 11/05/2026, 06:38:57
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        reach = 0
4
5        for i in range(len(nums)):
6            if reach < 0: return False
7
8            if nums[i] > reach:
9                reach = nums[i]
10            
11            reach -= 1
12        
13        return True