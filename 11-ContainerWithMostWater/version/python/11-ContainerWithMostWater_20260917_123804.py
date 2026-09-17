# Last updated: 17/09/2026, 12:38:04
1class Solution:
2    def maxArea(self, height: list[int]) -> int:
3        maxA = 0
4        l,  r = 0, len(height) - 1
5
6        while l < r:
7            maxA = max(maxA, min(height[l], height[r]) * (r - l))
8            
9            if height[l] > height[r]:
10                r = r - 1
11            else:
12                l = l + 1
13        
14        return maxA