// Last updated: 29/05/2026, 23:07:17
1class Solution {
2    public int[] plusOne(int[] digits) {
3        int lastDigit = digits.length - 1;
4        int carry = 0;
5        int sum = 0;
6
7        for (int i = lastDigit; i >= 0; i--) {
8            if (i == lastDigit) {
9                sum = digits[i] + 1;
10            } else {
11                sum = digits[i] + carry;
12            }
13
14            if (sum < 9) {
15                digits[i] = sum;
16                carry = 0;
17            } else {
18                digits[i] = sum % 10;
19                carry = sum / 10;
20            }
21        }
22
23        if (carry == 0) {
24            return digits;
25        } else {
26            int[] res = new int[digits.length + 1];
27            res[0] = 1;
28            
29            return res;
30        }
31    }
32}