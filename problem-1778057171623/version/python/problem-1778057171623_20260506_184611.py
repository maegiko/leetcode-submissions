# Last updated: 06/05/2026, 18:46:11
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
4
5        reverse_vowels = []
6        for i in range(len(s) - 1, -1, -1):
7            if s[i] in vowels:
8                reverse_vowels.append(s[i])
9        
10        print(reverse_vowels)
11        
12        s_copy = ""
13        vowel_idx = 0
14        for i in range(len(s)):
15            if s[i] in vowels:
16                s_copy += reverse_vowels[vowel_idx]
17                vowel_idx += 1
18            else:
19                s_copy += s[i]
20        
21        return s_copy
22
23