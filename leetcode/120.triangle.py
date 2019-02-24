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
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.minimumTotal_0(triangle)
    
    def minimumTotal_0(self, triangle: List[List[int]]) -> int:
        mem = {}
        import sys
        min_sum = sys.maxsize
        def bt(i: int, j: int, cur_sum: int) -> None:
            nonlocal mem, min_sum
            key = '{}-{}'.format(i, j)
            if key in mem and cur_sum >= mem[key]:
                return
            else:
                mem[key] = cur_sum
            cur_sum += triangle[i][j]
            if i == len(triangle) - 1:
                min_sum = min(min_sum, cur_sum)
                return
            bt(i+1, j, cur_sum)
            bt(i+1, j+1, cur_sum)
        bt(0, 0, 0)
        return min_sum
