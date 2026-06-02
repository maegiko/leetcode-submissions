# Last updated: 02/06/2026, 14:37:02
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
11                seen[dna] += 1
12            
13            seen[dna] = seen.get(dna, 0) + 1
14        
15        return res
16
17