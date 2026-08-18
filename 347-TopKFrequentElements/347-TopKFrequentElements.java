// Last updated: 18/08/2026, 14:56:21
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] bucket = new List[nums.length + 1];
        Arrays.setAll(bucket, i -> new ArrayList<>());
        HashMap<Integer, Integer> freq = new HashMap<>();

        for (int num : nums) {
            int value = freq.getOrDefault(num, 0);
            freq.put(num, value + 1);
        }

        freq.forEach((key, value) -> {
            bucket[value].add(key);
        });

        int[] res = new int[k];
        int index = 0;

        for (int i = bucket.length - 1; i > 0; i--) {
            for (int j : bucket[i]) {
                res[index] = j;
                index++;

                if (index >= k) {
                    return res;
                }
            }
        }

        return null;
    }
}