// Last updated: 18/08/2026, 14:57:00
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();

        while (n != 1) {
            int sum = 0;

            while (n > 0) {
                int ones = n % 10;
                sum += ones * ones;
                n = n / 10;
            }

            if (seen.contains(sum)) {
                return false;
            } else {
                seen.add(sum);
                n = sum;
            }
        }

        return true;
    }
}