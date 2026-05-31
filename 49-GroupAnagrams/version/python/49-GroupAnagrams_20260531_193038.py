# Last updated: 31/05/2026, 19:30:38
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        res = defaultdict(list)
4
5        for s in strs:
6            count = [0] * 26
7
8            for c in s:
9                count[ord(c) - ord('a')] += 1
10            
11            res[tuple(count)].append(s)
12        
13        return list(res.values())