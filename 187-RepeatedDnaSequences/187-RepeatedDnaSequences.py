# Last updated: 18/08/2026, 14:57:09
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = {}
        res = []

        for i in range(len(s) - 9):
            dna = s[i:i + 10]

            count = seen.get(dna, 0)

            if count == 1:
                res.append(dna)
            
            seen[dna] = count + 1
        
        return res

