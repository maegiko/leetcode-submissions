# Last updated: 10/05/2026, 16:23:56
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        res, count = 0, 0
4
5        for num in nums:
6            if count == 0:
7                res = num
8            
9            if res == num:
10                count += 1
11            else:
12                count -= 1
13        
14        return res