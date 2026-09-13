# Last updated: 13/09/2026, 13:06:15
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        maxL, maxR = height[0], height[-1]
4        res = 0
5        l, r = 0, len(height) - 1
6
7        while l < r:
8            if maxL > maxR:
9                r -= 1
10                maxR = max(maxR, height[r])
11                res += maxR - height[r]
12            else:
13                l += 1
14                maxL = max(maxL, height[l])
15                res += maxL - height[l]
16        
17        return res