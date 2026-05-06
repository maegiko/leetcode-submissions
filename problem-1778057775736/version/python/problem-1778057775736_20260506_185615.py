# Last updated: 06/05/2026, 18:56:15
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        s_idx = 0
4        if not s: return True
5
6        for i in range(len(t)):
7            if t[i] == s[s_idx]:
8                s_idx += 1
9                
10            if s_idx == len(s):
11                return True
12        
13        return False