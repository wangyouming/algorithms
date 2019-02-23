#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (58.80%)
# Total Accepted:    451K
# Total Submissions: 763.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepth_1(root) 
    
    def maxDepth_1(self, root: TreeNode) -> int:
        q = []
        ans = 0
        if root: q.append(root)
        while q:
            tmp = []
            for node in q:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            q = tmp
            ans += 1
        return ans            

    def maxDepth_0(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth_0(root.left), self.maxDepth_0(root.right)) + 1
