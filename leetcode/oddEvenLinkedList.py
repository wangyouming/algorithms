"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

URL: https://leetcode.com/problems/odd-even-linked-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_odd = ListNode(0)
        dummy_even = ListNode(0)
        parent_odd = dummy_odd
        parent_even = dummy_even
        node = head
        isOdd = False
        while node:
            isOdd = not isOdd
            if isOdd:
                parent_odd.next = node
                parent_odd = node
            else:
                parent_even.next = node
                parent_even = node
            node = node.next
        parent_even.next = None
        parent_odd.next = dummy_even.next
        return dummy_odd.next