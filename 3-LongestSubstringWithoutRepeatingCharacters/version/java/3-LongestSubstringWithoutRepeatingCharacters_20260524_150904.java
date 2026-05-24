// Last updated: 24/05/2026, 15:09:04
1class Solution {
2    public int lengthOfLongestSubstring(String s) {
3        int left = 0;
4        Set<Character> seen = new HashSet<>();
5        int length = 0;
6
7        for (int right = 0; right < s.length(); right++) {
8            while (seen.contains(s.charAt(right))) {
9                seen.remove(s.charAt(left));
10                left++;
11            }
12
13            seen.add(s.charAt(right));
14            length = Math.max(length, right - left + 1);
15        }
16
17        return length;
18    }
19}