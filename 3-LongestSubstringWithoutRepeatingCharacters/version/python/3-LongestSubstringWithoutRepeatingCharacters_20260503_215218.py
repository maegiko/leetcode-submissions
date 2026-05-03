# Last updated: 03/05/2026, 21:52:18
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left = 0
4        longest = 0
5        seen = set()
6
7        for right in range(len(s)):
8            while s[right] in seen:
9                seen.remove(s[left])
10                left += 1
11            
12            seen.add(s[right])
13            longest = max(longest, right - left + 1)
14        
15        return longest
16            
17