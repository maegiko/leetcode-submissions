// Last updated: 18/08/2026, 14:56:52
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int total = 0;
        int length = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++) {
            total += nums[right];

            while (total >= target) {
                length = Math.min(length, right - left + 1);
                total -= nums[left];
                left++;
            }
        }

        return (length == Integer.MAX_VALUE ? 0 : length);
    }
}