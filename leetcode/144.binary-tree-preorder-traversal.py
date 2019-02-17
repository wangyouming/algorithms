#
# @lc app=leetcode id=144 lang=python
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (49.95%)
# Total Accepted:    300.5K
# Total Submissions: 600.5K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,2,3]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.preorderTraversal_0(root)
        return self.preorderTraversal_1(root)
    
    def preorderTraversal_0(self, root):
        res = []
        cur = root
        stack = []
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop().right
        return res
    
    def preorderTraversal_1(self, root):
        stack = []
        if root: stack.append(root)
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
        return res
