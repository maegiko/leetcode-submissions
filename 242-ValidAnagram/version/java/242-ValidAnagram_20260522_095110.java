// Last updated: 22/05/2026, 09:51:10
1class Solution {
2    public boolean isAnagram(String s, String t) {
3        if (s.length() != t.length()) {
4            return false;
5        }
6
7        HashMap <Character, Integer> sMap = new HashMap<>();
8        HashMap <Character, Integer> tMap = new HashMap<>();
9
10        for (int i = 0; i < s.length(); i++) {
11            sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i), 0) + 1);
12            tMap.put(t.charAt(i), tMap.getOrDefault(t.charAt(i), 0) + 1);
13        }
14
15        return sMap.equals(tMap);
16    }
17}