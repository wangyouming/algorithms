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
        return self.postorderTraversal_1(root)

    def postorderTraversal_2(self, root):
        pre, p, s, res = None, root, [], []
        while p or s:
            while p:
                s.append(p)
                p = p.left
            p = s[-1]
            if not p.right or p.right is pre:
                res.append(p.val)
                s.pop()
                pre, p = p, None
            else:
                p = p.right
        return res
    
    def postorderTraversal_1(self, root):
        p, s, res = root, [], []
        while p or s:
            if p:
                s.append(p)
                res.insert(0, p.val)
                p = p.right
            else:
                p = s.pop()
                p = p.left
        return res

    def postorderTraversal_0(self, root):
        s, res = [], []
        if root: s.append(root)
        while s:
            p = s.pop()
            res.insert(0, p.val)
            if p.left: s.append(p.left)
            if p.right: s.append(p.right)
        return res
    