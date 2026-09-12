# Last updated: 12/09/2026, 13:27:04
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        maxArea = 0
5
6        for i, h in enumerate(heights):
7            append_i = i
8
9            while stack and stack[-1][1] > h:
10                s_i, s_h = stack.pop()
11                area = (i - s_i) * s_h
12                maxArea = max(area, maxArea)
13                append_i = s_i
14            
15            stack.append((append_i, h))
16        
17        maxWidth = len(heights)
18        while stack:
19            s_i, s_h = stack.pop()
20            area = (maxWidth - s_i) * s_h
21            maxArea = max(area, maxArea)
22        
23        return maxArea
24
25