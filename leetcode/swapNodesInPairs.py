"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

URL: https://leetcode.com/problems/swap-nodes-in-pairs/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        parent = dummy

        while parent and parent.next and parent.next.next:
            next = parent.next
            next_next = next.next
            next_next_next = next_next.next
            parent.next = next_next
            next_next.next = next
            next.next = next_next_next
            parent = next

        return dummy.next