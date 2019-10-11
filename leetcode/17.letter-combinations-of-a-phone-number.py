#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (41.77%)
# Likes:    2218
# Dislikes: 298
# Total Accepted:    397K
# Total Submissions: 950.4K
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# Example:
# 
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {'2': 'abc',
             '3': 'def',
             '4': 'ghi',
             '5': 'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'}
        def backtracing(cur_str, idx):
            if idx == len(digits):
                ans.append(cur_str)
            else:
                for c in m[digits[idx]]:
                    backtracing(cur_str + c, idx + 1)
        ans = []
        if digits:
            backtracing("", 0)
        return ans
