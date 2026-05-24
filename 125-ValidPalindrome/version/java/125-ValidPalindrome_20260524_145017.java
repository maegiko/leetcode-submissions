// Last updated: 24/05/2026, 14:50:17
1class Solution {
2    public boolean isPalindrome(String s) {
3        int left = 0;
4        int right = s.length() - 1;
5
6        while (left < right) {
7            while (!Character.isLetterOrDigit(s.charAt(left)) && left < right) {
8                left++;
9            }
10
11            while (!Character.isLetterOrDigit(s.charAt(right)) && left < right) {
12                right--;
13            }
14
15            if (left > right)
16                return false;
17
18            char leftChar = Character.toLowerCase(s.charAt(left));
19            char rightChar = Character.toLowerCase(s.charAt(right));
20
21            if (leftChar != rightChar) {
22                return false;
23            } else {
24                left++;
25                right--;
26            }
27        }
28
29        return true;
30    }
31}