// Last updated: 28/05/2026, 16:54:45
1class Solution {
2    public boolean isHappy(int n) {
3        String nStr = String.valueOf(n);
4        int total = n;
5
6        Map<String, Integer> map = new HashMap<>();
7        while (total != 1) {
8            int newTotal = 0;
9
10            for (int i = 0; i < nStr.length(); i++) {
11                int num = nStr.charAt(i) - '0';
12                newTotal += num * num;
13            }
14
15            if (map.get(nStr) != null && map.get(nStr) == newTotal)
16                return false;
17            else {
18                total = newTotal;
19                map.put(nStr, newTotal);
20                nStr = String.valueOf(newTotal);
21            }
22        }
23        
24        return true;
25    }
26}