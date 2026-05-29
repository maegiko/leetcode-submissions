// Last updated: 29/05/2026, 15:47:55
1class Solution {
2    public boolean isHappy(int n) {
3        Set<Integer> seen = new HashSet<>();
4
5        while (n != 1) {
6            int sum = 0;
7
8            while (n > 0) {
9                int ones = n % 10;
10                sum += ones * ones;
11                n = n / 10;
12            }
13
14            if (seen.contains(sum)) {
15                return false;
16            } else {
17                seen.add(sum);
18                n = sum;
19            }
20        }
21
22        return true;
23    }
24}