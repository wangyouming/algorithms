#
# @lc app=leetcode id=32 lang=python
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (24.76%)
# Total Accepted:    171.2K
# Total Submissions: 689.5K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        regions = []
        for idx, char in enumerate(s):
            if char == '(':
                stack.append((idx, char))
            else:
                if stack and stack[-1][1] == '(':
                    regions.append((stack[-1][0], idx))
                    while len(regions) >=2 and regions[-1][0] <= regions[-2][1]+1:
                        right = regions.pop()
                        left = regions.pop()
                        regions.append((min(right[0], left[0]), right[1]))
                    stack.pop()
                else:
                    stack.append((idx, char))
        ans = 0
        for region in regions:
            ans = max(region[1]-region[0]+1, ans)
        return ans

