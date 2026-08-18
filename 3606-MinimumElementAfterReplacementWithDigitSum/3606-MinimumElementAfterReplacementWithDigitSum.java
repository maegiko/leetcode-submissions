// Last updated: 18/08/2026, 14:55:44
class Solution {
    public int minElement(int[] nums) {
        int min = Integer.MAX_VALUE;

        for (int num : nums) {
            int digit = 0;
            int total = 0;

            while (num > 0) {
                digit = num % 10;
                total += digit;
                num = num / 10;
            }

            min = Math.min(min, total);
        }

        return min;
    }
}