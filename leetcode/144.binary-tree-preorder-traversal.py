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
        return self.preorderTraversal_3(root)

    def preorderTraversal_3(self, root):
        pre, cur, res = None, root, []
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    res.append(cur.val)
                    pre.right, cur = cur, cur.left
                else:
                    pre.right = None
                    cur = cur.right
        return res

    def preorderTraversal_2(self, root):
        p, s, res = root, [], []
        while p or s:
            if p:
                res.append(p.val)
                s.append(p)
                p = p.left
            else:
                p = s.pop()
                p = p.right
        return res

    def preorderTraversal_1(self, root):
        p, s, res = root, [], []
        while p or s:
            while p:
                res.append(p.val)
                s.append(p)
                p = p.left
            p = s.pop()
            p = p.right
        return res

    def preorderTraversal_0(self, root):
        s, res = [], []
        if root: s.append(root)
        while s:
            p = s.pop()
            res.append(p.val)
            if p.right: s.append(p.right)
            if p.left: s.append(p.left)
        return res
