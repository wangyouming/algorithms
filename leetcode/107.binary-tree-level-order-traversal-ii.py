#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (48.28%)
# Likes:    875
# Dislikes: 164
# Total Accepted:    254.2K
# Total Submissions: 523.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        return self.levelOrderBottom_1(root)

    # dfs
    def levelOrderBottom_1(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        def dfs(root: TreeNode, level: int):
            if level >= len(res):
                res.insert(0, [])
            
            res[-(level+1)].append(root.val)
            if root.left: dfs(root.left, level+1)
            if root.right: dfs(root.right, level+1)

        res = []
        dfs(root, 0)
        return res
    
    # bfs + queue
    def levelOrderBottom_0(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        from queue import Queue
        q, res = Queue(), []
        q.put(root)
        while not q.empty():
            res.insert(0, [])
            for _ in range(q.qsize()):
                node = q.get()
                res[0].append(node.val)
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
        return res
# @lc code=end