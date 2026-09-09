# Last updated: 09/09/2026, 13:50:54
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        num_set = set(nums)
4        longest = 0
5
6        for n in num_set:
7            count = 1
8            if n - 1 not in num_set:
9                while n + 1 in num_set:
10                    count += 1
11                    n = n + 1
12            
13            longest = max(longest, count)
14        
15        return longest