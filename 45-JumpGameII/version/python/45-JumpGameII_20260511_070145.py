# Last updated: 11/05/2026, 07:01:45
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        reach = 0
4        jumps = 0
5        goal = 0
6
7        for i in range(len(nums) - 1):
8            reach = max(reach, i + nums[i])
9
10            if i == goal:
11                goal = reach
12                jumps += 1
13        
14        return jumps