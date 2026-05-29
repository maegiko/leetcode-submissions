// Last updated: 29/05/2026, 20:59:49
1class Solution {
2    public int minElement(int[] nums) {
3        int min = Integer.MAX_VALUE;
4
5        for (int num : nums) {
6            int digit = 0;
7            int total = 0;
8
9            while (num > 0) {
10                digit = num % 10;
11                total += digit;
12                num = num / 10;
13            }
14
15            min = Math.min(min, total);
16        }
17
18        return min;
19    }
20}