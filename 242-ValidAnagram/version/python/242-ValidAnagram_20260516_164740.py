# Last updated: 16/05/2026, 16:47:40
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t): return False
4
5        s_count = {}
6        t_count = {}
7
8        for i in range(len(s)):
9            s_ltr = s[i]
10            t_ltr = t[i]
11
12            s_count[s_ltr] = s_count.get(s_ltr, 0) + 1
13            t_count[t_ltr] = t_count.get(t_ltr, 0) + 1
14        
15
16        return s_count == t_count