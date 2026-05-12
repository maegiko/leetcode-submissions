# Last updated: 13/05/2026, 00:27:08
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        words = s.split(" ")
4        
5        res = []
6
7        for i in range(len(words) - 1, -1, -1):
8            if words[i] != "":
9                res.append(words[i])
10        
11        return " ".join(res)