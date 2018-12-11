/*
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

URL: https://leetcode.com/problems/reverse-linked-list/
*/

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* reverseList_iteratively(ListNode *head) {
        ListNode *pre = head, *next = nullptr;
        while (head) {
            next = head->next;
            head->next = pre;
            pre = head;
            head = next;
        }
        return pre;
    }
    ListNode* reverseList_recursively(ListNode *head) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode *h = reverseList_recursively(head->next);
        head->next->next = head;
        head->next = nullptr;
        return h;
    }
    ListNode* reverseList(ListNode *head) {
        return reverseList_iteratively(head);
        return reverseList_recursively(head);
    }
};
