# Last updated: 09/04/2026, 21:46:29
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        charSet = set()
4        l = 0
5        longest = 0
6
7        for r in range(len(s)):
8            while s[r] in charSet:
9                charSet.remove(s[l])
10                l += 1
11            
12            charSet.add(s[r])
13            longest = max(longest, r - l + 1)
14        
15        return longest
16