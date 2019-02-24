#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (25.12%)
# Total Accepted:    354.9K
# Total Submissions: 1.4M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's
# value
# is 5 but its right child's value is 4.
# 
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBST_2(root)

    def isValidBST_2(self, root: TreeNode) -> bool:
        #inorder traversal
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val < inorder: return False
            inorder = root.val
            root = root.right
        return True

    def isValidBST_1(self, root: TreeNode) -> bool:
        if not root: return True
        stack = [(root, None, None)]
        while stack:
            node, lower_limit, upper_limit = stack.pop()
            if node.left:
                if node.left.val >= node.val: return False
                if lower_limit is not None and node.left.val <= lower_limit: return False
                stack.append((node.left, lower_limit, node.val))
            if node.right:
                if node.right.val <= node.val: return False
                if upper_limit is not None and node.right.val >= upper_limit: return False
                stack.append((node.right, node.val, upper_limit))

        return True

    def isValidBST_0(self, root: TreeNode) -> bool:
        def isValidBSTHelper(node: TreeNode, lower_limit, upper_limit) -> bool:
            if not node: return True
            if node.left:
                if node.left.val >= node.val: return False
                if lower_limit is not None and node.left.val <= lower_limit: return False
            if node.right:
                if node.right.val <= node.val: return False
                if upper_limit is not None and node.right.val >= upper_limit: return False
            return  isValidBSTHelper(node.left, lower_limit, node.val) and isValidBSTHelper(node.right, node.val, upper_limit) 
        return isValidBSTHelper(root, None, None)
