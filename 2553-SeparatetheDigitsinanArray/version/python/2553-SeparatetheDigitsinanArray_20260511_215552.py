# Last updated: 11/05/2026, 21:55:52
1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        res = []
4
5        for num in nums:
6            res.extend(int(j) for j in str(num))
7        
8        return res