# Last updated: 06/06/2026, 14:47:15
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        leftSum = [0] * len(nums)
4
5        runningSum = 0
6        for i in range(len(nums)):
7            leftSum[i] = runningSum
8            runningSum += nums[i]
9        
10        rightSum = [0] * len(nums)
11        counter = 0
12        for i in range(len(nums)):
13            counter += nums[i]
14            rightSum[i] = runningSum - counter
15        
16        res = [0] * len(nums)
17        for i in range(len(nums)):
18            res[i] = abs(leftSum[i] - rightSum[i])
19        
20        return res
21
22            
23
24            
25        