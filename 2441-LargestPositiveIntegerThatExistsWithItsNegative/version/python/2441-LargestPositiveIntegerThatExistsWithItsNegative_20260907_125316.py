# Last updated: 07/09/2026, 12:53:16
1class Solution:
2    def findMaxK(self, nums: List[int]) -> int:
3        seen = set()
4        largest = 0
5        res = 0
6
7        for num in nums:
8            if -(num) in seen:
9                positive = num if num > 0 else -(num)
10                if positive > largest:
11                    res = positive
12                    largest = positive
13
14            seen.add(num)
15        
16        return res if res != 0 else -1