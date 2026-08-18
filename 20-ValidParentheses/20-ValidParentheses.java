// Last updated: 18/08/2026, 14:58:27
class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> mappings = new HashMap<>();
        mappings.put(')', '(');
        mappings.put('}', '{');
        mappings.put(']', '[');

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (mappings.containsKey(c)) {
                if (stack.isEmpty() || !(stack.pop() == mappings.get(c))) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}