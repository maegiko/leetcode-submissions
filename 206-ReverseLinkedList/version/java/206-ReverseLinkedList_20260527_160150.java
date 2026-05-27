// Last updated: 27/05/2026, 16:01:50
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
12    public ListNode reverseList(ListNode head) {
13        if (head == null)
14            return null;
15
16        ListNode newHead = reverseList(head.next);
17
18        if (newHead == null) {
19            newHead = head;
20        } else {
21            head.next.next = head;
22            head.next = null;
23        }
24
25        return newHead;
26    }
27}