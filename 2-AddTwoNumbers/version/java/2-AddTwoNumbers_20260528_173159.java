// Last updated: 28/05/2026, 17:31:59
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
13        ListNode head1 = l1;
14        ListNode head2 = l2;
15        int carry = 0;
16
17        ListNode head = null;
18        ListNode current = null;
19        while (head1 != null || head2 != null || carry != 0) {
20            int val1 = head1 != null ? head1.val : 0;
21            int val2 = head2 != null ? head2.val : 0;
22
23            int total = val1 + val2 + carry;
24            int digit = total % 10;
25            carry = total / 10;
26
27            ListNode node = new ListNode(digit, null);
28
29            if (head == null) {
30                head = node;
31            } else {
32                current.next = node;
33            }
34            current = node;
35
36            if (head1 != null)
37                head1 = head1.next;
38            
39            if (head2 != null)
40                head2 = head2.next;
41        }
42
43        return head;
44    }
45}