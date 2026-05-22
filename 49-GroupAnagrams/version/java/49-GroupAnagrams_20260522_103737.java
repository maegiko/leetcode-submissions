// Last updated: 22/05/2026, 10:37:37
1class Solution {
2    public List<List<String>> groupAnagrams(String[] strs) {
3        HashMap<String, ArrayList<String>> map = new HashMap<>();
4
5        for (String s : strs) {
6            int[] count = new int[26];
7
8            for (char c : s.toCharArray()) {
9                count[c - 'a']++;
10            }
11
12            String key = Arrays.toString(count);
13            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
14        }
15
16        return new ArrayList<>(map.values());
17    }
18}