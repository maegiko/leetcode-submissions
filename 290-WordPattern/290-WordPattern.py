# Last updated: 18/08/2026, 14:56:35
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split(" ")

        if len(s_words) != len(pattern): return False

        pattern_map = {}
        s_map = {}

        for i in range(len(s_words)):
            if pattern[i] not in pattern_map and s_words[i] not in s_map:
                pattern_map[pattern[i]] = s_words[i]
                s_map[s_words[i]] = pattern[i]
            elif pattern[i] in pattern_map and pattern_map[pattern[i]] != s_words[i]: 
                return False
            elif s_words[i] in s_map and s_map[s_words[i]] != pattern[i]:
                return False 

        return True

