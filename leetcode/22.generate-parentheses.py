#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (55.22%)
# Likes:    2820
# Dislikes: 174
# Total Accepted:    346.6K
# Total Submissions: 627.5K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generateParenthesis_0(n)

    def generateParenthesis_1(self, n: int) -> List[str]:
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis_1(c):
                for right in self.generateParenthesis_1(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
    
    def generateParenthesis_0(self, n: int) -> List[str]:
        ans = []
        def backtrack(s: str, left: int, right: int):
            nonlocal n, ans
            if len(s) == n*2:
                ans.append(s)
            else:
                if left < n:
                    backtrack(s+'(', left+1, right)
                if left > right:
                    backtrack(s+')', left, right+1)
        backtrack('', 0, 0)
        return ans
