# Last updated: 09/05/2026, 15:25:10
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        k = 0
4        freq = {}
5
6        for i in range(len(nums)):
7            freq[nums[i]] = freq.get(nums[i], 0) + 1
8
9            if freq[nums[i]] <= 2:
10                nums[k] = nums[i]
11                k += 1
12        
13        return k