#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (42.72%)
# Total Accepted:    275.8K
# Total Submissions: 643.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy

        while current and current.next and current.next.next:
            next = current.next
            next_next = next.next
            next_next_next = next_next.next
            current.next = next_next
            next_next.next = next
            next.next = next_next_next
            current = next

        return dummy.next
