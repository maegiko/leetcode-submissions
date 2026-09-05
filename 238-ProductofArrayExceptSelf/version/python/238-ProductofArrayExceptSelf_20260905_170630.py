# Last updated: 05/09/2026, 17:06:30
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefix_prod = []
4        suffix_prod = [1] * len(nums)
5
6        total = 1
7        for num in nums:
8            prefix_prod.append(total)
9            total *= num
10        
11        total = 1
12        for i in range(len(nums) - 1, -1, -1):
13            suffix_prod[i] = total
14            total *= nums[i]
15        
16        res = []
17        for i in range(len(nums)):
18            res.append(prefix_prod[i] * suffix_prod[i])
19        
20        return res