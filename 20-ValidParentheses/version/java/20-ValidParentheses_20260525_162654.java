// Last updated: 25/05/2026, 16:26:54
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
14            } else if (mappings.containsKey(c)) {
15                if (stack.isEmpty() || !(stack.pop() == mappings.get(c))) {
16                    return false;
17                }
18            }
19        }
20
21        return stack.isEmpty();
22    }
23}