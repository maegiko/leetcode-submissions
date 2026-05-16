# Last updated: 16/05/2026, 16:41:14
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        s_words = s.split(" ")
4
5        if len(s_words) != len(pattern): return False
6
7        pattern_map = {}
8        s_map = {}
9
10        for i in range(len(s_words)):
11            if pattern[i] not in pattern_map and s_words[i] not in s_map:
12                pattern_map[pattern[i]] = s_words[i]
13                s_map[s_words[i]] = pattern[i]
14            elif pattern[i] in pattern_map and pattern_map[pattern[i]] != s_words[i]: 
15                return False
16            elif s_words[i] in s_map and s_map[s_words[i]] != pattern[i]:
17                return False 
18
19        return True
20
21