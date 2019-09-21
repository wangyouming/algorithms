#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (36.25%)
# Likes:    1958
# Dislikes: 283
# Total Accepted:    299.6K
# Total Submissions: 808.8K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            prev, slow, prev.next = slow, slow.next, prev

        tail = slow if not fast else slow.next
        head = slow
        isPalin = True
        while prev:
            isPalin = isPalin and prev.val == tail.val
            head, head.next, prev = prev, head, prev.next
            tail = tail.next
        return isPalin
