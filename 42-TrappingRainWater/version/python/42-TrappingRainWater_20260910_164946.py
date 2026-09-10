# Last updated: 10/09/2026, 16:49:46
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        l, r = 0, len(height) -1
4        maxL, maxR = height[l], height[r]
5        total = 0
6
7        while l < r:
8            if maxL < maxR:
9                l += 1
10                maxL = max(maxL, height[l])
11                total += maxL - height[l]
12            else:
13                r -= 1
14                maxR = max(maxR, height[r])
15                total += maxR - height[r]
16        
17        return total