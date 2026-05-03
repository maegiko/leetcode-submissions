# Last updated: 03/05/2026, 17:45:37
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        l = 0
4        longest = 0
5        seen = set()
6
7        for r in range(len(s)):
8            while s[r] in seen:
9                seen.remove(s[l])
10                l += 1
11            
12            seen.add(s[r])
13            longest = max(longest, r - l + 1)
14        
15        return longest
16