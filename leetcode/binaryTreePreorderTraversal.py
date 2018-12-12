"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

URL: https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        q = deque()
        q.append(root)
        ret = []
        while q:
            current = q.pop()
            ret.append(current.val)
            if current.right:
                q.append(current.right)
            if current.left:
                q.append(current.left)
        return ret