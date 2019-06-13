#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (51.00%)
# Likes:    594
# Dislikes: 1873
# Total Accepted:    234K
# Total Submissions: 457.9K
# Testcase Example:  '3'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
# 
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
# 
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# 
# Given an integer, convert it to a roman numeral. Input is guaranteed to be
# within the range from 1 to 3999.
# 
# Example 1:
# 
# 
# Input: 3
# Output: "III"
# 
# Example 2:
# 
# 
# Input: 4
# Output: "IV"
# 
# Example 3:
# 
# 
# Input: 9
# Output: "IX"
# 
# Example 4:
# 
# 
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# 
# 
# Example 5:
# 
# 
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
#
class Solution:
    def intToRoman(self, num: int) -> str:
        m = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        nums = [1000, 500, 100, 50, 10, 5, 1]
        res, index = '', 0
        while num != 0:
            count = num // nums[index]
            num = num % nums[index]
            res += m[nums[index]]*count
            if nums[index] == 1000 and num >= 900:
                res += 'CM'
                num -= 900
                index += 2
            elif nums[index] == 500 and num >= 400:
                res += 'CD'
                num -= 400
                index += 1
            elif nums[index] == 100 and num >= 90:
                res += 'XC'
                num -= 90
                index += 2
            elif nums[index] == 50 and num >= 40:
                res += 'XL'
                num -= 40
                index += 1
            elif nums[index] == 10 and num >= 9:
                res += 'IX'
                num -= 9
                index += 2
            elif nums[index] == 5 and num >= 4:
                res += 'IV'
                num -= 4
                index += 1
            else:
                index += 1

        return res
