# Last updated: 10/09/2026, 15:38:27
1class Solution:
2    def maxArea(self, heights: List[int]) -> int:
3        mostWater = 0
4        i = 0
5        j = len(heights) - 1
6
7        while i < j:
8            area = (j - i) * min(heights[i], heights[j])
9            mostWater = max(mostWater, area)
10
11            if heights[i] < heights[j]:
12                i += 1
13            elif heights[j] < heights[i]:
14                j -= 1
15            else:
16                i += 1
17                j -= 1
18        
19        return mostWater