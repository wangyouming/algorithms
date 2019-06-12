#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.31%)
# Likes:    3671
# Dislikes: 354
# Total Accepted:    568K
# Total Submissions: 2.1M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        max_range = (0, 0)
        for i in range(1, len(s)):
            max_len = max_range[1] - max_range[0] + 1
            if self.isPalindrome(s, i-max_len-1, i):
                max_range = (i-max_len-1, i)
            elif self.isPalindrome(s, i-max_len, i):
                max_range = (i-max_len, i)
        return s[max_range[0]: max_range[1]+1]
    
    def isPalindrome(self, s: str, begin: int, end: int) -> bool:
        if begin < 0: return False
        for i in range((end-begin+1)//2):
            if s[begin+i] != s[end-i]: return False
        return True
