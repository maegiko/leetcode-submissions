// Last updated: 29/05/2026, 16:14:48
1class Solution {
2    public boolean containsNearbyDuplicate(int[] nums, int k) {
3        Map<Integer, Integer> seen = new HashMap<>();
4
5        for (int j = 0; j < nums.length; j++) {
6            if (seen.containsKey(nums[j])) {
7                int i = seen.get(nums[j]);
8                int diff = Math.abs(i - j);
9
10                if (diff <= k)
11                    return true;
12            }
13
14            seen.put(nums[j], j);
15        }
16        
17        return false;
18
19    }
20}