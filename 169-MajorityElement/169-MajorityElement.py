# Last updated: 18/08/2026, 14:57:11
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for num in nums:
            if count == 0:
                res = num
            
            if res == num:
                count += 1
            else:
                count -= 1
        
        return res