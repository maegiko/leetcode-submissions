# Last updated: 01/06/2026, 13:46:08
1class Solution:
2    def minElement(self, nums: List[int]) -> int:
3        min_num = float("inf")
4
5        for num in nums:
6            sum_digits = 0
7
8            while num > 0:
9                digit = num % 10
10                sum_digits += digit
11                num //= 10
12            
13            min_num = min(min_num, sum_digits)
14        
15        return min_num