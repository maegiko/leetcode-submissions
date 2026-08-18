// Last updated: 18/08/2026, 14:56:54
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null)
            return null;

        ListNode newHead = reverseList(head.next);

        if (newHead == null) {
            newHead = head;
        } else {
            head.next.next = head;
            head.next = null;
        }

        return newHead;
    }
}