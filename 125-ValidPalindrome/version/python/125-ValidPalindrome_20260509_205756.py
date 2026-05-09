# Last updated: 09/05/2026, 20:57:56
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        l, r = 0, len(s) - 1
4
5        while l < r:
6            while l < r and (not s[l].isalnum() or not s[r].isalnum()):
7                if s[l].isalnum() is False:
8                    l += 1
9                
10                if s[r].isalnum() is False:
11                    r -= 1
12
13            if l >= r:
14                return True
15
16            if s[l].lower() == s[r].lower():
17                l += 1
18                r -= 1
19            else:
20                return False
21        
22        return True