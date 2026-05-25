// Last updated: 25/05/2026, 17:30:19
1class Solution {
2    public int search(int[] nums, int target) {
3        int left = 0;
4        int right = nums.length - 1;
5
6        while (left <= right) {
7            int middle = (left + right) / 2;
8
9            if (target > nums[middle]) {
10                left = middle + 1;
11            } else if (target < nums[middle]) {
12                right = middle - 1;
13            } else {
14                return middle;
15            }
16        }
17
18        return -1;
19    }
20}