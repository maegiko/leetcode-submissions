# Last updated: 15/09/2026, 12:21:04
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        seen = set()
5        res = []
6
7        for i, n in enumerate(nums):
8            if n in seen:
9                continue
10            
11            l, r = i + 1, len(nums) - 1
12
13            while l < r:
14                if n + nums[l] + nums[r] < 0:
15                    l += 1
16                elif n + nums[l] + nums[r] > 0:
17                    r -= 1
18                else:
19                    res.append([n, nums[l], nums[r]])
20
21                    lVal = nums[l]
22                    rVal = nums[r]
23                    while l < len(nums) and nums[l] == lVal:
24                        l += 1
25
26                    while r >= 0 and nums[r] == rVal:
27                        r -= 1
28            
29            seen.add(n)
30        
31        return res
32