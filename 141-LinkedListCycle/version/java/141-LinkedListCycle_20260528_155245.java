// Last updated: 28/05/2026, 15:52:45
1/**
2 * Definition for singly-linked list.
3 * class ListNode {
4 *     int val;
5 *     ListNode next;
6 *     ListNode(int x) {
7 *         val = x;
8 *         next = null;
9 *     }
10 * }
11 */
12public class Solution {
13    public boolean hasCycle(ListNode head) {
14        if (head == null) 
15            return false;
16
17        Set<ListNode> seen = new HashSet<>();
18
19        ListNode node = head;
20        while (node.next != null) {
21            if (seen.contains(node.next)) {
22                return true;
23            }
24            
25            seen.add(node);
26            node = node.next;
27        }
28
29        return false;
30    }
31}