/*
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
*/

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode *post = &dummy;
        while (n > 0 && post) {
            post = post->next;
            --n;
        }
        if (post == nullptr) return nullptr;
        ListNode *pre = &dummy;
        while (post->next) {
            pre = pre->next;
            post = post->next;
        }

        if (pre->next) {
            pre->next = pre->next->next;
        }
        return dummy.next;
    }
};