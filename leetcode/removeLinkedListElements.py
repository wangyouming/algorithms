"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

URL: https://leetcode.com/problems/remove-linked-list-elements/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        parent = dummy
        while parent.next:
            if parent.next.val == val:
                parent.next = parent.next.next
            else:
                parent = parent.next
        return dummy.next