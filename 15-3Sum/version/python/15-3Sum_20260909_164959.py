# Last updated: 09/09/2026, 16:49:59
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        seen = set()
5        res = []
6
7        for i in range(len(nums)):
8            if nums[i] in seen:
9                continue
10            
11            l = i + 1
12            r = len(nums) - 1
13
14            while l < r:
15                l_val = nums[l]
16                r_val = nums[r]
17                val = l_val + r_val
18
19                if val < -(nums[i]):
20                    while l + 1 < len(nums) and nums[l] == l_val:
21                        l += 1
22                elif val > -(nums[i]):
23                    while r - 1 >= 0 and nums[r] == r_val:
24                        r -= 1
25                else:
26                    triplet = [nums[l], nums[r], nums[i]]
27                    res.append(triplet)
28                    while l + 1 < len(nums) and nums[l] == l_val:
29                        l += 1
30                    
31                    while r - 1 >= 0 and nums[r] == r_val:
32                        r -= 1
33            
34            seen.add(nums[i])
35        
36        return res