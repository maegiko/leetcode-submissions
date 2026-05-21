// Last updated: 22/05/2026, 09:43:45
1class Solution {
2    public boolean containsDuplicate(int[] nums) {
3        HashSet<Integer> set = new HashSet<>();
4
5        for (int num : nums) {
6            if (set.contains(num)) {
7                return true;
8            } else {
9                set.add(num);
10            }
11        }
12
13        return false;
14    }
15}