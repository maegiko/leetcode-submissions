# Last updated: 07/09/2026, 12:32:17
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
4        operators = ['+', '-', '*', '/']
5
6        res = tokens[0]
7        for t in tokens:
8            if t in operators:
9                val1 = int(stack.pop())
10                val2 = int(stack.pop())
11
12                if t == '+':
13                    res = val1 + val2
14                elif t == '-':
15                    res = val2 - val1
16                elif t == '*':
17                    res = val1 * val2
18                else:
19                    res = val2 / val1
20                
21                stack.append(res)
22            else:
23                stack.append(t)
24        
25        return int(res)
26                        