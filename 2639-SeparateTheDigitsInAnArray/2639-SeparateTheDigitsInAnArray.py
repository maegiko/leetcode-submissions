# Last updated: 18/08/2026, 14:55:32
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            res.extend(int(j) for j in str(num))
        
        return res