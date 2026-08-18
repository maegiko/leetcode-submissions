// Last updated: 18/08/2026, 14:56:46
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int j = 0; j < nums.length; j++) {
            if (seen.containsKey(nums[j])) {
                int i = seen.get(nums[j]);
                int diff = Math.abs(i - j);

                if (diff <= k)
                    return true;
            }

            seen.put(nums[j], j);
        }
        
        return false;

    }
}