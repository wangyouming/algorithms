"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

URL: https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        curr = root
        stack = []
        while curr or stack:
            if curr:
                res.insert(0, curr.val)
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop().left
        return res