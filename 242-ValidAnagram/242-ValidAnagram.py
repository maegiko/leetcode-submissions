# Last updated: 18/08/2026, 14:56:43
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_ltr = s[i]
            t_ltr = t[i]

            s_count[s_ltr] = s_count.get(s_ltr, 0) + 1
            t_count[t_ltr] = t_count.get(t_ltr, 0) + 1
        

        return s_count == t_count