#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (40.55%)
# Total Accepted:    350.8K
# Total Submissions: 863.6K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
# 
#
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits: return []
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            s = digits[i] + carry
            if s < 10:
                digits[i] = s
                carry = 0
                break
            else:
                digits[i] = s % 10
                carry = 1
        return digits if carry == 0 else [1] + digits

