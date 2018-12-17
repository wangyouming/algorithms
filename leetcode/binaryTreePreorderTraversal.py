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
        return self.preorderTraversal_1(root)

    def preorderTraversal_1(self, root):
        cur = root
        ret = []
        stack = [] #等待处理右节点的节点
        while cur or stack:
            if cur:
                stack.append(cur)
                ret.append(cur.val)
                cur = cur.left
            else:
                cur = stack.pop().right
        return ret

    def preorderTraversal_0(self, root):
        if not root: return []
        stack = [root] #等待处理的节点
        ret = []
        while stack:
            current = stack.pop()
            ret.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return ret