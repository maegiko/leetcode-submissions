# Last updated: 02/06/2026, 14:31:49
1class Solution:
2    def findRepeatedDnaSequences(self, s: str) -> List[str]:
3        seen = set()
4        added = set()
5        res = []
6
7        for i in range(len(s) - 9):
8            dna = s[i:i + 10]
9
10            if dna in seen and dna not in added:
11                res.append(dna)
12                added.add(dna)
13            
14            seen.add(dna)
15        
16        return res
17
18