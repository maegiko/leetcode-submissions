// Last updated: 25/05/2026, 16:47:13
1class MinStack {
2    private Deque<Integer> stack;
3    private Deque<Integer> minStack;
4
5    public MinStack() {
6        this.stack = new ArrayDeque<>();
7        this.minStack = new ArrayDeque<>();
8    }
9    
10    public void push(int val) {
11        stack.push(val);
12
13        if (minStack.isEmpty() || val <= minStack.peek()) {
14            minStack.push(val);
15        }
16    }
17    
18    public void pop() {
19        int value = stack.pop();
20
21        if (minStack.peek() == value) {
22            minStack.pop();
23        }
24    }
25    
26    public int top() {
27        return stack.peek();
28    }
29    
30    public int getMin() {
31        return minStack.peek();
32    }
33}
34
35/**
36 * Your MinStack object will be instantiated and called as such:
37 * MinStack obj = new MinStack();
38 * obj.push(val);
39 * obj.pop();
40 * int param_3 = obj.top();
41 * int param_4 = obj.getMin();
42 */