"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

Note:

The total number of elements of the given matrix will not exceed 10,000.

URL: https://leetcode.com/problems/diagonal-traverse/
"""

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: 
            return []
        res = []
        import collections
        dd = collections.defaultdict(list)
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i+j].append(matrix[i][j])
        for i in range(0, len(matrix) + len(matrix[0]) - 1):
            if i % 2 == 0:
                res.extend(reversed(dd[i]))
            else:
                res.extend(dd[i])
        return res

print(Solution().findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))