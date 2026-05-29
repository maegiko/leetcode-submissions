// Last updated: 29/05/2026, 23:11:55
1class Solution {
2    public int[] plusOne(int[] digits) {
3        for (int i = digits.length - 1; i >= 0; i--) {
4            if (digits[i] < 9) {
5                digits[i]++;
6                return digits;
7            }
8
9            digits[i] = 0;
10        }
11
12        int[] res = new int[digits.length + 1];
13        res[0] = 1;
14        return res;
15    }
16}