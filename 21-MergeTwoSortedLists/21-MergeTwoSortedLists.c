// Last updated: 08/04/2026, 12:40:10
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {

    struct ListNode new;
    struct ListNode *new_current = &new;

    new.next = NULL;

    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            new_current->next = list1;
            list1 = list1->next;
        } else {
            new_current->next = list2;
            list2 = list2->next;
        }
        new_current = new_current->next;
    }

    new_current->next = (list1 != NULL) ? list1 : list2;

    return new.next;

}