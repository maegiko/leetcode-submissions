# Last updated: 26/08/2026, 18:59:48
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        res = []
4        total = 0
5
6        for num in nums:
7            total += num
8            res.append(total)
9        
10        return res