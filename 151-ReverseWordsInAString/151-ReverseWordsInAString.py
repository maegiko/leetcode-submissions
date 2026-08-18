# Last updated: 18/08/2026, 14:57:18
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        
        res = []

        for i in range(len(words) - 1, -1, -1):
            if words[i] != "":
                res.append(words[i])
        
        return " ".join(res)