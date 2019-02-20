#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (32.50%)
# Total Accepted:    336K
# Total Submissions: 1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.mergeKLists_2(lists)

    def mergeKLists_2(self, lists):
        def merge2Lists(l1, l2):
            dummy = current = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l1
                    l1 = current.next.next
                current = current.next 
            current.next = l1 if l1 else l2
            return dummy.next
        
        #Divide and Conquer
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount-interval, interval*2):
                lists[i] = merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if amount > 0 else lists
    
    def mergeKLists_1(self, lists):
        dummy = current = ListNode(0)
        from Queue import PriorityQueue
        q = PriorityQueue()
        for l in lists:
            if l: q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            current.next = ListNode(val)
            current = current.next
            node = node.next
            if node:
                q.put((node.val, node))
        return dummy.next

    def mergeKLists_0(self, lists):
        vals = []
        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next
        vals.sort()
        dummy = current = ListNode(0)
        for val in vals:
            current.next = ListNode(val)
            current = current.next
        return dummy.next