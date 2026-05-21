// Last updated: 22/05/2026, 09:39:57
1class Solution {
2    public int[] twoSum(int[] nums, int target) {
3        HashMap<Integer, Integer> map = new HashMap<>();
4
5        for (int i = 0; i < nums.length; i++) {
6            int diff = target - nums[i];
7
8            if (map.containsKey(diff)) {
9                return new int[] {map.get(diff), i};
10            } else {
11                map.put(nums[i], i);
12            }
13        }
14
15        return null;
16    }
17}