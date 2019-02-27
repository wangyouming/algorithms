#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (38.07%)
# Total Accepted:    168.5K
# Total Submissions: 440.6K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.minimumTotal_1(triangle)

    def minimumTotal_1(self, triangle: List[List[int]]) -> int:
        dp = [0] * len(triangle[-1])
        for i in range(len(triangle)):
            for j in range(i, -1, -1):
                if j == 0: dp[j] = dp[j] + triangle[i][j]
                elif j == i: dp[j] = dp[j-1] + triangle[i][j]
                else: dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
        return min(dp)

    def minimum_total_0(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

    