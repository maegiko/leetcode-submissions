// Last updated: 24/05/2026, 14:52:56
1class Solution {
2    public boolean isPalindrome(String s) {
3        int left = 0;
4        int right = s.length() - 1;
5
6        while (left < right) {
7            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
8                left++;
9            }
10
11            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
12                right--;
13            }
14
15            char leftChar = Character.toLowerCase(s.charAt(left));
16            char rightChar = Character.toLowerCase(s.charAt(right));
17
18            if (leftChar != rightChar) {
19                return false;
20            } else {
21                left++;
22                right--;
23            }
24        }
25
26        return true;
27    }
28}