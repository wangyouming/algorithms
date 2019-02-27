#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (54.58%)
# Total Accepted:    402K
# Total Submissions: 734.6K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorderTraversal_1(root)

    def inorderTraversal_2(self, root):
        res = []
        stack = []
        if root: stack.append((root, False))
        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                if node.right: stack.append((node.right, False))
                stack.append((node, True))
                if node.left: stack.append((node.left, False))
        return res

    def inorderTraversal_1(self, root):
        stack = []
        res = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right
        return res
    
    def inorderTraversal_0(self, root):
        def helper(node, res):
            if not node: return
            if node.left: helper(node.left, res)
            res.append(node.val)
            if node.right: helper(node.right, res)
        res = []
        helper(root, res)
        return res
