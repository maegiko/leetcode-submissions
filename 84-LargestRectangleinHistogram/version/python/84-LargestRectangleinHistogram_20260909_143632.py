# Last updated: 09/09/2026, 14:36:32
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        max_area = 0
5
6        for i in range(len(heights)):
7            pop_idx = i
8
9            while stack and stack[-1][1] > heights[i]:
10                idx, height = stack.pop()
11                width = i - idx
12                area = width * height
13                max_area = max(max_area, area)
14                pop_idx = idx
15                
16            stack.append((pop_idx, heights[i]))
17        
18        max_width = len(heights)
19        while stack:
20            idx, height = stack.pop()
21            width = max_width - idx
22            area = height * width
23            max_area = max(max_area, area)
24        
25        return max_area
26