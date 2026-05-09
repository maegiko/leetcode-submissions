# Last updated: 09/05/2026, 17:29:25
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        k = k % len(nums)
7        shifts = []
8        num_shifts = k - 1
9
10        for i in range(len(nums)):
11            if (i == (len(nums) - 1) - num_shifts):
12                shifts.append(nums[i])
13                num_shifts -= 1
14                nums[i] = None
15
16        right = len(nums) - 1
17        for i in range(len(nums) - 1, -1, -1):
18            if nums[i] is not None:
19                nums[right], nums[i] = nums[i], nums[right]
20                right -= 1
21        
22        for i in range(0, k):
23            nums[i] = shifts[i]
24
25
26    
27        
28
29
30        