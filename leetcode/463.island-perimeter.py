#
# @lc app=leetcode id=463 lang=python
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (60.04%)
# Total Accepted:    120.2K
# Total Submissions: 199.9K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
# 
# 
# 
# Example:
# 
# 
# Input:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
# 
#
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m = len(grid)
        n = len(grid[0])
        cell_cnt = 0
        neighbor_cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cell_cnt += 1
                    if i < m-1 and grid[i+1][j] == 1: neighbor_cnt += 1
                    if j < n-1 and grid[i][j+1] == 1: neighbor_cnt += 1
        return cell_cnt*4 - neighbor_cnt*2