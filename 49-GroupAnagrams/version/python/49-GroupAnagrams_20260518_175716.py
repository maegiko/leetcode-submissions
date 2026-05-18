# Last updated: 18/05/2026, 17:57:16
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        res = defaultdict(list)
4
5        for s in strs:
6            count = [0] * 26
7            for c in s:
8                count[ord(c) - ord("a")] += 1
9            
10            res[tuple(count)].append(s)
11
12        return list(res.values())