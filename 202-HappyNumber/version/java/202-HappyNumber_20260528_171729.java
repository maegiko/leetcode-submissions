// Last updated: 28/05/2026, 17:17:29
1class Solution {
2    public boolean isHappy(int n) {
3        Set<Integer> seen = new HashSet<>();
4
5        int total = n;
6        while (total != 1) {
7            int digit = total;
8            int newTotal = 0;
9            
10            while (total != 0) {
11                digit = total % 10;
12                total = total / 10;
13                newTotal += digit * digit;
14            }
15
16            if (seen.contains(newTotal)) {
17                return false;
18            } else {
19                seen.add(newTotal);
20                total = newTotal;
21            }
22        }
23
24        return true;
25    }
26}