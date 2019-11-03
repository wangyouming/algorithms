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
        return self.inorderTraversal_3(root)

    def inorderTraversal_3(self, root):
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
                    pre.right, cur = cur, cur.left
                else:
                    pre.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res

    def inorderTraversal_2(self, root):
        p, s, res = root, [], []
        while p or s:
            if p:
                s.append(p)
                p = p.left
            else:
                p = s.pop()
                res.append(p.val)
                p = p.right
        return res

    def inorderTraversal_1(self, root):
        p, s, res = root, [], []
        while p or s:
            while p:
                s.append(p)
                p = p.left
            p = s.pop()
            res.append(p.val)
            p = p.right
        return res
    
    def inorderTraversal_0(self, root):
        def inorder(node, res):
            if not node: return
            if node.left: inorder(node.left, res)
            res.append(node.val)
            if node.right: inorder(node.right, res)

        res = []
        inorder(root, res)
        return res
