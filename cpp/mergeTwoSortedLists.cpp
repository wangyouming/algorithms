/*
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

URL: https://leetcode.com/problems/merge-two-sorted-lists/
*/

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode dummy = ListNode(0);
        ListNode *pre = &dummy;
        while (true) {
            if (l1 == nullptr) {
                pre->next = l2;
                break;
            }
            if (l2 == nullptr) {
                pre->next = l1;
                break;
            }
            if (l1->val <= l2->val) {
                pre->next = l1;
                l1 = l1->next;
            } else {
                pre->next = l2;
                l2 = l2->next;
            }
            pre = pre->next;
        }

        return dummy.next;
    }
};
