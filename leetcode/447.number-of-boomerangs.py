#
# @lc app=leetcode id=447 lang=python
#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (48.87%)
# Total Accepted:    50K
# Total Submissions: 102.1K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# 
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
# 
#
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_cnt = 0
        for i in range(len(points)):
            mem = {}
            for j in range(len(points)):
                if i == j: continue
                dis = self.dis([points[i], points[j]])
                if dis in mem: mem[dis] = mem[dis] + 1
                else: mem[dis] = 1
            for cnt in mem.values():
                if cnt > 1: total_cnt += (cnt*(cnt-1))
        return total_cnt
    
    def dis(self, points):
        return pow(points[0][0] - points[1][0], 2) + pow(points[0][1] - points[1][1], 2)
        
