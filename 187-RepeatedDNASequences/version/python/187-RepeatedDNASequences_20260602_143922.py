# Last updated: 02/06/2026, 14:39:22
1class Solution:
2    def findRepeatedDnaSequences(self, s: str) -> List[str]:
3        seen = {}
4        res = []
5
6        for i in range(len(s) - 9):
7            dna = s[i:i + 10]
8
9            count = seen.get(dna, 0)
10
11            if count == 1:
12                res.append(dna)
13            
14            seen[dna] = count + 1
15        
16        return res
17
18