#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (43.12%)
# Total Accepted:    352.7K
# Total Submissions: 814.2K
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairs_1(n)
    
    def climbStairs_1(self, n: int) -> int:
        mem = {}
        mem[0], mem[1], mem[2] = 1, 1, 2
        for i in range(3, n+1):
            mem[i] = mem[i-1] + mem[i-2]
        return mem[n]
    
    def climbStairs_0(self, n: int) -> int:
        mem = {}
        mem[0] = 1
        mem[1] = 1
        mem[2] = 2
        def climbStairs(n: int) -> int:
            if n in mem: return mem[n]
            ans = climbStairs(n-1) + climbStairs(n-2)
            mem[n] = ans
            return ans
        return climbStairs(n)
