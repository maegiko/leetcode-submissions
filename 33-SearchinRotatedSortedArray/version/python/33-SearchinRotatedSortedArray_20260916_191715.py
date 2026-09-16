# Last updated: 16/09/2026, 19:17:15
1class Solution:
2    def search(self, nums: list[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            mid = (l + r) // 2
7
8            if nums[mid] == target:
9                return mid
10            
11            if nums[l] <= nums[mid]:
12                if target > nums[mid] or target < nums[l]:
13                    l = mid + 1
14                else:
15                    r = mid - 1
16            else:
17                if target < nums[mid] or target > nums[r]:
18                    r = mid - 1
19                else:
20                    l = mid + 1
21        
22        return -1