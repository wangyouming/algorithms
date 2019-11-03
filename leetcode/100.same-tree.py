#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (50.77%)
# Likes:    1352
# Dislikes: 45
# Total Accepted:    429.2K
# Total Submissions: 842.3K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
# 
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
# 
# Example 1:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# Output: false
# 
# 
# Example 3:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# Output: false
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.isSameTree_1(p, q)
        
    def isSameTree_0(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q: return p.val == q.val and \
                           self.isSameTree(p.left, q.left) and \
                           self.isSameTree(p.right, q.right)
        else:
            return p is q
    
    def isSameTree_1(self, p: TreeNode, q: TreeNode) -> bool:
        s0, s1 = [], []
        if p: s0.append(p)
        if q: s1.append(q)
        while s0 and s1:
            n0, n1 = s0.pop(), s1.pop()
            if n0.val != n1.val: return False

            if n0.left: s0.append(n0.left)
            if n1.left: s1.append(n1.left)
            if len(s0) != len(s1): return False
        
            if n0.right: s0.append(n0.right)
            if n1.right: s1.append(n1.right)
            if len(s0) != len(s1): return False
        
        return len(s0) == len(s1)
# @lc code=end