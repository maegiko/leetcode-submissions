// Last updated: 24/05/2026, 14:39:23
1class Solution {
2    public boolean isPalindrome(String s) {
3        String formatted = "";
4
5        for (char c : s.toCharArray()) {
6            if (Character.isLetterOrDigit(c)) {
7                formatted += Character.toLowerCase(c);
8            }
9        }
10
11        int left = 0;
12        int right = formatted.length() - 1;
13
14        while (left <= right) {
15            if (!(formatted.charAt(left) == formatted.charAt(right))) {
16                return false;
17            } else {
18                left++;
19                right--;
20            }
21        }
22
23        return true;
24    }
25}