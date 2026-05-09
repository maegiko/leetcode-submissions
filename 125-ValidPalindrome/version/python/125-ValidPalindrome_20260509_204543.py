# Last updated: 09/05/2026, 20:45:43
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        string = ""
4        for char in s:
5            if char.isalnum():
6                string += char.lower()
7
8        l, r = 0, len(string) - 1
9
10        while l < r:
11            if string[l] == string[r]:
12                l += 1
13                r -= 1
14            else:
15                return False
16        
17        return True