// Last updated: 29/05/2026, 22:49:18
1class Solution {
2    public int[] plusOne(int[] digits) {
3        boolean digitIncrease = true;
4
5        for (int i = 0; i < digits.length; i++) {
6            if (digits[i] != 9)
7                digitIncrease = false;
8        }
9
10        int digitLen = digitIncrease ? digits.length + 1 : digits.length;
11
12        int[] res = new int[digitLen];
13
14        int carry = 0;
15        int insertIdx = digitLen - 1;
16        for (int i = digits.length - 1; i >= 0; i--) {
17            if (i == digits.length - 1) {
18                int total = digits[i] + 1;
19                int digit = total % 10;
20                res[insertIdx] = digit;
21                carry = total / 10;
22            } else {
23                int total = digits[i] + carry;
24                int digit = total % 10;
25                res[insertIdx] = digit;
26                carry = total / 10;
27            }
28            insertIdx--;
29        }
30
31        if (digitLen > digits.length) {
32            res[0] += carry;
33        }
34
35        return res;
36    }
37}