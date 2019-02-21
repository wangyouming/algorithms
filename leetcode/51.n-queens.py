#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (37.29%)
# Total Accepted:    127.9K
# Total Submissions: 341.2K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
# 
# Example:
# 
# 
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
# 
# 
#
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        queens = ['.' * n for _ in range(n)]
        res = []
        def isValid(row, col):
            top_left = col - 1
            top_right = col + 1
            for i in range(row-1, -1, -1):
                if queens[i][col] == 'Q': return False
                if top_left >= 0 and queens[i][top_left] == 'Q': return False
                if top_right < n and queens[i][top_right] == 'Q': return False
                top_left -= 1
                top_right += 1
            return True

        def dfs(row):
            if row == n:
                res.append(queens[:])
                return
            for col in range(n):
                if isValid(row, col):
                    s = list(queens[row])
                    s[col] = 'Q'
                    queens[row] = ''.join(s)
                    dfs(row+1)
                    s[col] = '.'
                    queens[row] = ''.join(s)
        
        dfs(0)
        return res
        