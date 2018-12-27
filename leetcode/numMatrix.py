"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:

You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.

URL: https://leetcode.com/problems/range-sum-query-2d-immutable/
"""

class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix: return
        rows = len(matrix)
        cols = len(matrix[0])
        self.sum = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    self.sum[row][col] = matrix[row][col]
                elif row == 0:
                    self.sum[row][col] = self.sum[row][col-1] + matrix[row][col]
                elif col == 0:
                    self.sum[row][col] = self.sum[row-1][col] + matrix[row][col]
                else:
                    self.sum[row][col] = self.sum[row-1][col] + self.sum[row][col-1] - self.sum[row-1][col-1] + matrix[row][col]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.sum[row2][col2]
        elif row1 == 0:
            return self.sum[row2][col2] - self.sum[row2][col1-1]
        elif col1 == 0:
            return self.sum[row2][col2] - self.sum[row1-1][col2]
        else:
            return self.sum[row2][col2] - self.sum[row1-1][col2] - self.sum[row2][col1-1] + self.sum[row1-1][col1-1]
        
if __name__ == '__main__':
    matrix = matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    m = NumMatrix(matrix)
    assert(m.sumRegion(2, 1, 4, 3) == 8)
    assert(m.sumRegion(1, 1, 2, 2) == 11)
    assert(m.sumRegion(2, 1, 4, 3) == 8)
    assert(m.sumRegion(1, 2, 2, 4) == 12)
    print('hello world')

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
