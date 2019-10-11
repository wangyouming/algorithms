#
# @lc app=leetcode id=498 lang=python
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (44.82%)
# Total Accepted:    36.6K
# Total Submissions: 81.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
# 
# 
# 
# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
#
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        res = []
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, 0
        top_right = True
        while True:
            res.append(matrix[i][j])
            if i == m-1 and j == n-1: break
            if top_right:
                if i == 0 and j == n - 1:
                    i += 1
                    top_right = not top_right
                elif i == 0:
                    j += 1
                    top_right = not top_right
                elif j == n - 1: 
                    i += 1
                    top_right = not top_right
                else:
                    i -= 1
                    j += 1
            else:
                if i == m-1 and j == 0:
                    j += 1
                    top_right = not top_right
                elif i == m-1:
                    j += 1
                    top_right = not top_right
                elif j == 0:
                    i += 1
                    top_right = not top_right
                else:
                    i += 1
                    j -= 1
        return res
        