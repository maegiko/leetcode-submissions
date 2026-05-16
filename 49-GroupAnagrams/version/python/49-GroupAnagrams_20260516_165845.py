# Last updated: 16/05/2026, 16:58:45
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        groups = defaultdict(list)
4
5        for s in strs:
6            count = [0] * 26
7            for c in s:
8                count[ord(c) - ord('a')] += 1
9            
10            groups[tuple(count)].append(s)
11        
12        return list(groups.values())
13