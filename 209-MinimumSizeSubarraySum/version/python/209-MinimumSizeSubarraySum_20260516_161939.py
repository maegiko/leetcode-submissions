# Last updated: 16/05/2026, 16:19:39
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        total = 0
4        left = 0
5        min_len = float("inf")
6
7        for right in range(len(nums)):
8            total += nums[right]
9
10            while total >= target:
11                min_len = min(min_len, right - left + 1)
12                total -= nums[left]
13                left += 1
14        
15        return 0 if min_len == float("inf") else min_len
16