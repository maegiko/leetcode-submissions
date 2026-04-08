# Last updated: 08/04/2026, 20:20:08
1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        magazineFreq = {}
4        ransomFreq = {}
5
6        for i in range(len(magazine)):
7            magazineFreq[magazine[i]] = magazineFreq.get(magazine[i], 0) + 1
8        
9        for i in range(len(ransomNote)):
10            ransomFreq[ransomNote[i]] = ransomFreq.get(ransomNote[i], 0) + 1
11            if ransomNote[i] not in magazineFreq or ransomFreq[ransomNote[i]] > magazineFreq[ransomNote[i]]:
12                return False
13        
14        return True
15