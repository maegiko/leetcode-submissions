// Last updated: 08/04/2026, 12:39:51
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode new;
    new.next = NULL;

    if (head == NULL) {
        return new.next;
    }

    int length = 0;
    struct ListNode *current = head;

    while (current != NULL) {
        length++;
        current = current->next;
    }

    int middle = (length + 1) / 2;

    int count = 1;
    current = head;

    while (current != NULL && count != middle) {
        current = current->next;
        count++;
    }
    
    if (length % 2 == 0) {
        new.next = current->next;
    } else {
        new.next = current;
    }

    return new.next;


    
}