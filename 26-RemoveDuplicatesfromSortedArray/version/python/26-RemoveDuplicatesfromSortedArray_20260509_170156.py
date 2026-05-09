# Last updated: 09/05/2026, 17:01:56
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        res = 0
4        count = 0
5
6        for num in nums:
7            if count == 0:
8                res = num
9            
10            if res == num:
11                count += 1
12            else:
13                count -= 1
14        
15        return res