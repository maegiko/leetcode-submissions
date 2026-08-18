# Last updated: 18/08/2026, 14:56:17
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineFreq = {}
        ransomFreq = {}

        for i in range(len(magazine)):
            magazineFreq[magazine[i]] = magazineFreq.get(magazine[i], 0) + 1
        
        for i in range(len(ransomNote)):
            ransomFreq[ransomNote[i]] = ransomFreq.get(ransomNote[i], 0) + 1
            if ransomNote[i] not in magazineFreq or ransomFreq[ransomNote[i]] > magazineFreq[ransomNote[i]]:
                return False
        
        return True
