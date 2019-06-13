#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.54%)
# Likes:    1381
# Dislikes: 1329
# Total Accepted:    475.2K
# Total Submissions: 1.4M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sz, ret = zip(*strs), ''
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret
