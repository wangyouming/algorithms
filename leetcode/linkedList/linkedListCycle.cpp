/*
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

URL: https://leetcode.com/problems/linked-list-cycle/
*/

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr) return false;
        ListNode *walker = head;
        ListNode *runner = head;
        while (walker && runner && runner->next) {
            walker = walker->next;
            runner = runner->next->next;
            if (walker == runner) {
                return true;
            }
        }
        return false;
    }
};