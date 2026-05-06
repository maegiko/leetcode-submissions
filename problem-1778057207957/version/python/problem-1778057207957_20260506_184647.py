# Last updated: 06/05/2026, 18:46:47
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
4
5        reverse_vowels = []
6        for i in range(len(s) - 1, -1, -1):
7            if s[i] in vowels:
8                reverse_vowels.append(s[i])
9        
10        s_copy = ""
11        vowel_idx = 0
12        for i in range(len(s)):
13            if s[i] in vowels:
14                s_copy += reverse_vowels[vowel_idx]
15                vowel_idx += 1
16            else:
17                s_copy += s[i]
18        
19        return s_copy
20
21