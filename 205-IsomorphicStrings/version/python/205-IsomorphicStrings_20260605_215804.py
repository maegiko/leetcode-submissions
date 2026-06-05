# Last updated: 05/06/2026, 21:58:04
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        s_to_t = {}
4        t_to_s = {}
5
6        for i in range(len(s)):
7            char_s = s[i]
8            char_t = t[i]
9
10            if char_s in s_to_t:
11                if s_to_t[char_s] != char_t:
12                    return False
13            else:
14                s_to_t[char_s] = char_t
15            
16            if char_t in t_to_s:
17                if t_to_s[char_t] != char_s:
18                    return False
19            else:
20                t_to_s[char_t] = char_s
21        
22        return True
23
24
25
26
27
28
29
30