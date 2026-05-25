// Last updated: 25/05/2026, 16:24:20
1class Solution {
2    public boolean isValid(String s) {
3        Deque<Character> stack = new ArrayDeque<>();
4        Map<Character, Character> mappings = new HashMap<>();
5        mappings.put(')', '(');
6        mappings.put('}', '{');
7        mappings.put(']', '[');
8
9        for (int i = 0; i < s.length(); i++) {
10            char c = s.charAt(i);
11
12            if (c == '(' || c == '{' || c == '[') {
13                stack.push(c);
14            }
15
16            if (mappings.containsKey(c)) {
17                if (!stack.isEmpty()) {
18                    char val = stack.pop();
19                    if (val != mappings.get(c))
20                        return false;
21                } else {
22                    return false;
23                }
24            }
25        }
26
27        return stack.isEmpty() ? true : false;
28    }
29}