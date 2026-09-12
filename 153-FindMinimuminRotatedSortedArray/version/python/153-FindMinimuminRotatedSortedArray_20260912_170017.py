# Last updated: 12/09/2026, 17:00:17
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0, len(nums) - 1
4
5        if nums[l] < nums[r]:
6            return nums[l]
7        else:
8            minVal = nums[r]
9
10            while l <= r:
11                mid = (l + r) // 2
12                
13                if nums[mid] > minVal:
14                    l = mid + 1
15                else:
16                    r = mid - 1
17                    minVal = min(minVal, nums[mid])
18
19            return minVal
20
21
22