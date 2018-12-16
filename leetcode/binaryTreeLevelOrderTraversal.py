"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root: return []
    
        level = [root]
        res = []
        while level:
            res.append([node.val for node in level])
            tmp = []
            for node in level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            level = tmp

        return res
