# Last updated: 18/08/2026, 14:56:14
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        if not s: return True

        for i in range(len(t)):
            if t[i] == s[s_idx]:
                s_idx += 1
                
            if s_idx == len(s):
                return True
        
        return False