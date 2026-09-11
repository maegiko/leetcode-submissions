# Last updated: 11/09/2026, 12:11:22
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stack = []
4        res = [0] * len(temperatures)
5
6        for i, t in enumerate(temperatures):
7            while stack and t > temperatures[stack[-1]]:
8                s_idx = stack.pop()
9                res[s_idx] = i - s_idx
10            
11            stack.append(i)
12        
13        return res
14