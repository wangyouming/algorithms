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
        mem = [(0, 0)] * len(s)
        mem[0] = (0, 0)
        for i in range(1, len(s)):
            pre_begin, pre_end = mem[i-1]
            pre_len = pre_end - pre_begin + 1
            if self.isPalindrome(s, i-pre_len-1, i):
                mem[i] = (i-pre_len-1, i)
            elif self.isPalindrome(s, i-pre_len, i):
                mem[i] = (i-pre_len, i)
            else:
                mem[i] = mem[i-1]

        begin, end = mem[-1]
        return s[begin:end+1]
    
    def isPalindrome(self, s: str, begin: int, end: int) -> bool:
        if begin < 0: return False
        for i in range((end-begin+1)//2):
            if s[begin+i] != s[end-i]: return False
        return True


input = "cbbd"
print(Solution().longestPalindrome(input))