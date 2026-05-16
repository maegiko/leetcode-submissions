# Last updated: 16/05/2026, 16:30:14
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        jumps, max_reach, current_end = 0, 0, 0
4
5        for i in range(len(nums) - 1):
6            max_reach = max(max_reach, i + nums[i])
7
8            if i == current_end:
9                jumps += 1
10                current_end = max_reach
11        
12        return jumps
13
14