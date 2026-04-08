# Last updated: 08/04/2026, 20:02:05
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        words = s.split(" ")
4
5        lastWordIdx = len(words) - 1
6        lastWord = words[lastWordIdx]
7
8        while lastWord == " " or lastWord == "":
9            lastWordIdx -= 1
10            lastWord = words[lastWordIdx]
11
12        return len(lastWord)