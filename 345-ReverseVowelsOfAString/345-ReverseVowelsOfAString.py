# Last updated: 18/08/2026, 14:56:22
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        reverse_vowels = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] in vowels:
                reverse_vowels.append(s[i])
        
        s_copy = []
        vowel_idx = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s_copy.append(reverse_vowels[vowel_idx])
                vowel_idx += 1
            else:
                s_copy.append(s[i])
        
        return "".join(s_copy)

