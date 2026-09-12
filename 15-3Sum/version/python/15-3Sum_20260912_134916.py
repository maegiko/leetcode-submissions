# Last updated: 12/09/2026, 13:49:16
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
20                    l += 1
21                elif val > -(nums[i]):
22                    r -= 1
23                else:
24                    triplet = [nums[l], nums[r], nums[i]]
25                    res.append(triplet)
26                    while l + 1 < len(nums) and nums[l] == l_val:
27                        l += 1
28                    
29                    while r - 1 >= 0 and nums[r] == r_val:
30                        r -= 1
31            
32            seen.add(nums[i])
33        
34        return res