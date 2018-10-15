/*
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

URL: https://leetcode.com/problems/reverse-linked-list-ii/
*/

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode new_head = ListNode(0);
        new_head.next = head;
        ListNode *pre = &new_head;
        for (int i = 0; i < m - 1; i++) {
            pre = pre->next;
        }
        ListNode *cur = pre->next;
        for (int i = 0; i < n-m; i++) {//不断交换相邻的两个
            ListNode *move = cur->next;
            cur->next = move->next;
            move->next = pre->next;
            pre->next = move;
        }

        return new_head.next;
    }
};
