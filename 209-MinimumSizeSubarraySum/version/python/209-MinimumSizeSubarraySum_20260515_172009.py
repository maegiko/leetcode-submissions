# Last updated: 15/05/2026, 17:20:09
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        total = 0
4        left = 0
5        min_len = 0
6
7        for right in range(len(nums)):
8            total += nums[right]
9            
10            while total >= target:
11                if min_len == 0:
12                    min_len = right - left + 1
13                else:
14                    min_len = min(min_len, right - left + 1)
15
16                total -= nums[left]
17                left += 1
18        
19        return min_len
20