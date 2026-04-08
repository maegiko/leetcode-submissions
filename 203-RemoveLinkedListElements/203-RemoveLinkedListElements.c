// Last updated: 08/04/2026, 12:39:58
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    if (head == NULL) return NULL;

    struct ListNode *new = removeElements(head->next, val);

    if (head->val == val) {
        return new;
    } else {
        head->next = new;
        return head;
    }
}