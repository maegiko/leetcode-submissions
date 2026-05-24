// Last updated: 24/05/2026, 15:22:25
1class Solution {
2    public int minSubArrayLen(int target, int[] nums) {
3        int left = 0;
4        int total = 0;
5        int length = Integer.MAX_VALUE;
6
7        for (int right = 0; right < nums.length; right++) {
8            total += nums[right];
9
10            while (total >= target) {
11                length = Math.min(length, right - left + 1);
12                total -= nums[left];
13                left++;
14            }
15        }
16
17        return (length == Integer.MAX_VALUE ? 0 : length);
18    }
19}