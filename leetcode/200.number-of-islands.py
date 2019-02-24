#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (39.91%)
# Total Accepted:    299.9K
# Total Submissions: 746.5K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        m = len(grid)
        n = len(grid[0])
        sum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                else:
                    stack = []
                    stack.append([i, j])
                    sum += 1
                    while stack:
                        [p, q] = stack.pop()
                        if p >= 1 and grid[p-1][q] == '1':
                            stack.append([p-1, q])
                        if p < m - 1 and grid[p+1][q] == '1':
                            stack.append([p+1, q])
                        if q >= 1 and grid[p][q-1] == '1':
                            stack.append([p, q-1])
                        if q < n - 1 and grid[p][q+1] == '1':
                            stack.append([p, q+1])
                        grid[p][q] = '0'
        return sum
