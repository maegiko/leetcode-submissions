# Last updated: 13/05/2026, 17:02:11
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        nums = {
4            "I": 1,
5            "V": 5,
6            "X": 10,
7            "L": 50,
8            "C": 100,
9            "D": 500,
10            "M": 1000
11        }
12
13        num = 0
14        i = 0
15        while i < len(s):
16            if i < len(s) - 1 and s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
17                num += nums[s[i + 1]] - 1
18                i += 2
19            elif i < len(s) - 1 and s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
20                num += nums[s[i + 1]] - 10
21                i += 2
22            elif i < len(s) - 1 and s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
23                num += nums[s[i + 1]] - 100
24                i += 2
25            else:
26                num += nums[s[i]]
27                i += 1
28        
29        return num
30                
31