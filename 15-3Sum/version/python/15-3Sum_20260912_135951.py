# Last updated: 12/09/2026, 13:59:51
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        res = []
5
6        for i, n in enumerate(nums):
7            if i - 1 >= 0 and n == nums[i - 1]:
8                continue
9            
10            l = i + 1
11            r = len(nums) - 1
12
13            while l < r:
14                total = nums[l] + nums[r]
15                l_val = nums[l]
16                r_val = nums[r]
17
18                if total > -(n):
19                    r -= 1
20                elif total < -(n):
21                    l += 1
22                else:
23                    res.append([n, nums[l], nums[r]])
24                    while l + 1 < len(nums) and nums[l] == l_val:
25                        l += 1
26                    
27                    while r - 1 >= 0 and nums[r] == r_val:
28                        r -= 1
29
30        return res
31
32
33