#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (46.44%)
# Total Accepted:    232.7K
# Total Submissions: 499.4K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.postorderTraversal_0(root)
        return self.postorderTraversal_1(root)
    
    def postorderTraversal_1(self, root):
        res = []
        stack = []
        if root: stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)
        return res[::-1]

    def postorderTraversal_0(self, root):
        res = []
        stack = []
        if root: stack.append((root, False))
        while stack:
            node, visted = stack.pop()
            if visted:
                res.append(node.val)
            else:
                stack.append((node, True))
                if node.right: stack.append((node.right, False))
                if node.left: stack.append((node.left, False))
        return res
    