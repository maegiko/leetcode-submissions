# Last updated: 05/09/2026, 17:34:16
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        xor = 0
4        for num in nums:
5            xor = xor ^ num
6        
7        return xor
8