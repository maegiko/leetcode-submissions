// Last updated: 18/08/2026, 14:58:22
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> map = new HashMap<>();

        for (String s : strs) {
            int[] count = new int[26];

            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            String key = Arrays.toString(count);
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(map.values());
    }
}