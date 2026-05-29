// Last updated: 29/05/2026, 16:03:09
1/**
2 * Definition for singly-linked list.
3 * public class ListNode {
4 *     int val;
5 *     ListNode next;
6 *     ListNode() {}
7 *     ListNode(int val) { this.val = val; }
8 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
9 * }
10 */
11class Solution {
12    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
13        int carry = 0;
14        ListNode head = null;
15        ListNode current = head;
16
17        while (l1 != null || l2 != null || carry != 0) {
18            int val1 = l1 != null ? l1.val : 0;
19            int val2 = l2 != null ? l2.val : 0;
20
21            int sum = val1 + val2 + carry;
22            int ones = sum % 10;
23            carry = sum / 10;
24
25            ListNode newNode = new ListNode(ones, null);
26
27            if (head == null) {
28                head = newNode;
29                current = head;
30            } else {
31                current.next = newNode;
32                current = current.next;
33            }
34
35            if (l1 != null) {
36                l1 = l1.next;
37            }
38
39            if (l2 != null) {
40                l2 = l2.next;
41            }
42        }
43
44        return head;
45    }
46}
47