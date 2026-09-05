# Last updated: 05/09/2026, 17:53:07
1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        prefix_max = []
4        suffix_min = [1] * len(nums)
5
6        running_max = nums[0]
7        running_min = nums[-1]
8
9        for num in nums:
10            running_max = max(running_max, num)
11            prefix_max.append(running_max)
12        
13        for i in range(len(nums) - 1, -1, -1):
14            running_min = min(running_min, nums[i])
15            suffix_min[i] = running_min
16
17        min_stable = float(inf)
18        for i in range(len(nums)):
19            instability = prefix_max[i] - suffix_min[i]
20
21            if instability <= k:
22                min_stable = min(i, min_stable)
23        
24        return min_stable if min_stable != float(inf) else -1
25        
26    
27    