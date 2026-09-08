# Last updated: 08/09/2026, 13:30:54
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        res = [0] * len(temperatures)
4        stack = []
5
6        for i in range(len(temperatures)):
7            while stack and stack[-1][0] < temperatures[i]:
8                temp, idx = stack.pop()
9                res[idx] = i - idx
10            
11            stack.append([temperatures[i], i])
12        
13        return res