# Last updated: 02/06/2026, 14:37:32
1class Solution:
2    def findRepeatedDnaSequences(self, s: str) -> List[str]:
3        seen = {}
4        res = []
5
6        for i in range(len(s) - 9):
7            dna = s[i:i + 10]
8
9            if dna in seen and seen[dna] == 1:
10                res.append(dna)
11            
12            seen[dna] = seen.get(dna, 0) + 1
13        
14        return res
15
16