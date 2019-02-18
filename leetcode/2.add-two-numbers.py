#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.39%)
# Total Accepted:    754.5K
# Total Submissions: 2.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        current = dummy
        carry = 0

        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val / 10
            val = val % 10
            current.next = ListNode(val)
            current = current.next
            l1 = l1.next
            l2 = l2.next

        while l1 or l2:
            node = l1 if l1 else l2
            val = node.val + carry
            carry = val / 10
            val = val % 10
            current.next = ListNode(val)
            current = current.next
            if l1: l1 = l1.next
            else: l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)
            current = current.next

        current.next = None
        return dummy.next
        
