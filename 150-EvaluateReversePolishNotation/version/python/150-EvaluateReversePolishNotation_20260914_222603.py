# Last updated: 14/09/2026, 22:26:03
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
4
5        for t in tokens:
6            if t != '+' and t != '-' and t != '*' and t != '/':
7                stack.append(t)
8            else:
9                val1 = int(stack.pop())
10                val2 = int(stack.pop())
11
12                if t == '+':
13                    stack.append(val2 + val1)
14                elif t == '-':
15                    stack.append(val2 - val1)
16                elif t == '*':
17                    stack.append(val1 * val2)
18                else:
19                    stack.append(val2 / val1)
20        
21        return int(stack.pop())