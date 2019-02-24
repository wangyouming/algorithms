#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (45.17%)
# Total Accepted:    207.7K
# Total Submissions: 457.4K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.minPathSum_0(grid)
    
    def minPathSum_0(self, grid: List[List[int]]) -> int:
        mem = {}
        def dp(row: int, col: int) -> int:
            nonlocal mem
            key = '{}-{}'.format(row, col)
            if key in mem: return mem[key]

            if row == 0 and col == 0: 
                return grid[0][0]
            elif col == 0: 
                ans = dp(row-1, col) + grid[row][col]
            elif row == 0: 
                ans = dp(row, col-1) + grid[row][col]
            else:
                ans = min(dp(row-1, col), dp(row, col-1)) + grid[row][col]
            mem[key] = ans
            return ans
        return dp(len(grid)-1, len(grid[0])-1)
