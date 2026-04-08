# Last updated: 08/04/2026, 20:10:34
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        index = len(s) - 1
4        lastChar = s[index]
5
6        while lastChar == " ":
7            index -= 1
8            lastChar = s[index]
9        
10        count = 0
11        while s[index] != " " and index >= 0:
12            count += 1
13            index-= 1
14        
15        return count
16