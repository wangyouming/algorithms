"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

URL: https://leetcode.com/problems/set-matrix-zeroes/
"""

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.setZeroes_1(matrix)

    def setZeroes_1(self, matrix):
        if not matrix: return
        m = len(matrix)
        n = len(matrix[0]) 
        rowHasZero = False
        for i in range(0, n):
            if matrix[0][i] == 0:
                rowHasZero = True
                break

        colHasZero = False
        for i in range(0, m):
            if matrix[i][0] == 0:
                colHasZero = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if rowHasZero:
            for i in range(n):
                matrix[0][i] = 0
        if colHasZero:
            for i in range(m):
                matrix[i][0] = 0

    def setZeroes_0(self, matrix):
        if not matrix: return
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        
if __name__ == '__main__':
    solution = Solution()

    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    res = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    solution.setZeroes(matrix)
    assert(matrix == res)

    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    res = [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]
    ]
    solution.setZeroes(matrix)
    assert(matrix == res)
