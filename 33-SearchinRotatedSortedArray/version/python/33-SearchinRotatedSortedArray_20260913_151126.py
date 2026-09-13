# Last updated: 13/09/2026, 15:11:26
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            mid = (l + r) // 2
7
8            if nums[mid] == target:
9                return mid
10
11            # mid belongs to the left portion of the array
12            if nums[l] <= nums[mid]:
13                if target > nums[mid] or target < nums[l]:
14                    l = mid + 1
15                else:
16                    r = mid - 1
17            # mid is in the right portion of the array
18            else:
19                if target < nums[mid] or target > nums[r]:
20                    r = mid - 1
21                else:
22                    l = mid + 1
23        
24        return -1
25
26