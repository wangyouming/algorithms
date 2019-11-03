#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (37.01%)
# Likes:    1553
# Dislikes: 129
# Total Accepted:    157.8K
# Total Submissions: 421.9K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(i, j) -> List[TreeNode]:
            if j < i: return [None]
            else:
                res = []
                for k in range(i, j+1):
                    lefts, rights = generate(i, k-1), generate(k+1, j)
                    for left in lefts:
                        for right in rights:
                            root = TreeNode(k)
                            root.left, root.right = left, right
                            res.append(root)
                return res

        if n == 0: return []
        return generate(1, n)
# @lc code=end