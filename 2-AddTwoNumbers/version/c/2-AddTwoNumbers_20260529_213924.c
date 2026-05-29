// Last updated: 29/05/2026, 21:39:24
1/**
2 * Definition for singly-linked list.
3 * struct ListNode {
4 *     int val;
5 *     struct ListNode *next;
6 * };
7 */
8struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
9    struct ListNode *head = NULL;
10    struct ListNode *curr = NULL;
11    int carry = 0;
12
13    while (l1 || l2 || carry != 0) {
14        int val1 = (l1 != NULL) ? l1->val : 0;
15        int val2 = (l2 != NULL) ? l2->val : 0;
16
17        int total = val1 + val2 + carry;
18        int ones = total % 10;
19        carry = total / 10;
20
21        struct ListNode *node = malloc(sizeof(struct ListNode));
22        node->val = ones;
23        node->next = NULL;
24
25        if (!head) {
26            head = node;
27            curr = node;
28        } else {
29            curr->next = node;
30            curr = curr->next;
31        }
32
33        if (l1) {
34            l1 = l1->next;
35        }
36
37        if (l2) {
38            l2 = l2->next;
39        }
40    }
41
42    return head;
43}