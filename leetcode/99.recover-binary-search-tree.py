#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (35.72%)
# Likes:    996
# Dislikes: 58
# Total Accepted:    132.5K
# Total Submissions: 366.6K
# Testcase Example:  '[1,3,null,null,2]'
#
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# Example 1:
# 
# 
# Input: [1,3,null,null,2]
# 
# 1
# /
# 3
# \
# 2
# 
# Output: [3,1,null,null,2]
# 
# 3
# /
# 1
# \
# 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,4,null,null,2]
# 
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
# 
# Output: [2,1,4,null,null,3]
# 
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
# 
# 
# Follow up:
# 
# 
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?
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
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.recoverTree_3(root)

    def recoverTree_3(self, root: TreeNode) -> None:
        parent, cur, first, second = None, root, None, None
        while cur:
            if not cur.left:
                if parent and parent.val > cur.val:
                    if not first: first = parent
                    second = cur
                parent, cur = cur, cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur: pre = pre.right
                if not pre.right:
                    pre.right, cur = cur, cur.left
                else:
                    pre.right = None
                    if pre.val > cur.val:
                        if not first: first = pre
                        second = cur
                    parent, cur = cur, cur.right

        if first and second: first.val, second.val = second.val, first.val
    
    def recoverTree_2(self, root: TreeNode) -> None:
        pre, first, second = None, None, None
        p, s = root, []
        while p or s:
            if p:
                s.append(p)
                p = p.left
            else:
                cur = s.pop()
                if pre and pre.val > cur.val:
                    if not first: first = pre
                    second = cur
                pre, p = cur, cur.right

        if first and second: first.val, second.val = second.val, first.val

    def recoverTree_1(self, root: TreeNode) -> None:
        pre, first, second = None, None, None
        p, s = root, []
        while p or s:
            while p:
                s.append(p)
                p = p.left
            cur = s.pop()
            if pre and pre.val > cur.val:
                if not first: first = pre
                second = cur
            pre, p = cur, cur.right

        if first and second: first.val, second.val = second.val, first.val

    def recoverTree_0(self, root: TreeNode) -> None:
        nodes, vals = [], []

        def inorder(root: TreeNode):
            if not root: return
            if root.left: inorder(root.left)
            nodes.append(root)
            vals.append(root.val)
            if root.right: inorder(root.right)

        inorder(root)
        vals.sort()
        for idx, node in enumerate(nodes):
            node.val = vals[idx]
# @lc code=end