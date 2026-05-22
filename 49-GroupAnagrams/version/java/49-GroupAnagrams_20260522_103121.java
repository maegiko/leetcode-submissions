// Last updated: 22/05/2026, 10:31:21
1class Solution {
2    public List<List<String>> groupAnagrams(String[] strs) {
3        HashMap<String, ArrayList<String>> map = new HashMap<>();
4
5        for (String s : strs) {
6            List<Integer> count = new ArrayList<>(Collections.nCopies(26, 0));
7
8            for (int i = 0; i < s.length(); i++) {
9                int index = (int) s.charAt(i) - (int) 'a';
10                int amt = count.get(index);
11                count.set(index, amt + 1);
12            }
13            
14            String key = count.toString();
15            if (map.get(key) == null) {
16                ArrayList<String> words = new ArrayList<>();
17                words.add(s);
18                map.put(key, words);
19            } else {
20                map.get(key).add(s);
21            }
22        }
23
24        return new ArrayList<>(map.values());
25    }
26}