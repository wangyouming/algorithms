"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

URL: https://leetcode.com/problems/partition-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_0 = ListNode(0)
        parent_0 = dummy_0
        dummy_1 = ListNode(0)
        parent_1 = dummy_1
        
        node = head
        while node: 
            if node.val < x:
                parent_0.next = node
                parent_0 = node
            else:
                parent_1.next = node
                parent_1 = node
            node = node.next
        parent_1.next = None
        parent_0.next = dummy_1.next
        
        return dummy_0.next