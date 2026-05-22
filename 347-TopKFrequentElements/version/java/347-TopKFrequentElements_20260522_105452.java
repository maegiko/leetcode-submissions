// Last updated: 22/05/2026, 10:54:52
1class Solution {
2    public int[] topKFrequent(int[] nums, int k) {
3        List<Integer>[] bucket = new List[nums.length + 1];
4        Arrays.setAll(bucket, i -> new ArrayList<>());
5        HashMap<Integer, Integer> freq = new HashMap<>();
6
7        for (int num : nums) {
8            int value = freq.getOrDefault(num, 0);
9            freq.put(num, value + 1);
10        }
11
12        freq.forEach((key, value) -> {
13            bucket[value].add(key);
14        });
15
16        int[] res = new int[k];
17        int index = 0;
18
19        for (int i = bucket.length - 1; i > 0; i--) {
20            for (int j : bucket[i]) {
21                res[index] = j;
22                index++;
23
24                if (index >= k) {
25                    return res;
26                }
27            }
28        }
29
30        return null;
31    }
32}