#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (52.17%)
# Total Accepted:    504.5K
# Total Submissions: 963.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseListIteratively(head)
        return self.reverseListRecursively(head)
        
    def reverseListIteratively(self, head):
        pre = None
        current = head
        while current:
            next = current.next
            current.next = pre
            pre = current
            current = next
        return pre
    
    def reverseListRecursively(self, head):
        if not head or not head.next: return head
        new_head = self.reverseListRecursively(head.next)
        head.next.next = head
        head.next = None
        return new_head
            
