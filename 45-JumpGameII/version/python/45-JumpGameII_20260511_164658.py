# Last updated: 11/05/2026, 16:46:58
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        jumps = 0
4        reach = 0
5        currentEnd = 0
6
7        for i in range(len(nums) - 1):
8            reach = max(reach, i + nums[i])
9
10            if i == currentEnd:
11                jumps += 1
12                currentEnd = reach
13        
14
15        return jumps