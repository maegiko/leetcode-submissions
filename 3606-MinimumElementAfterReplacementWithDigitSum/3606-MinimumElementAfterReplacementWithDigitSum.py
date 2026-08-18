# Last updated: 18/08/2026, 14:55:37
class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_num = float("inf")

        for num in nums:
            sum_digits = 0

            while num > 0:
                digit = num % 10
                sum_digits += digit
                num //= 10
            
            min_num = min(min_num, sum_digits)
        
        return min_num