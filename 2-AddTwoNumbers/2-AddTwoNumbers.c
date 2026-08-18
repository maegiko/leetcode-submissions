// Last updated: 18/08/2026, 14:58:37
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *head = NULL;
    struct ListNode *curr = NULL;
    int carry = 0;

    while (l1 || l2 || carry != 0) {
        int val1 = (l1 != NULL) ? l1->val : 0;
        int val2 = (l2 != NULL) ? l2->val : 0;

        int total = val1 + val2 + carry;
        int ones = total % 10;
        carry = total / 10;

        struct ListNode *node = malloc(sizeof(struct ListNode));
        node->val = ones;
        node->next = NULL;

        if (!head) {
            head = node;
            curr = node;
        } else {
            curr->next = node;
            curr = curr->next;
        }

        if (l1) {
            l1 = l1->next;
        }

        if (l2) {
            l2 = l2->next;
        }
    }

    return head;
}