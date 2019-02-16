#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (62.63%)
# Total Accepted:    365.1K
# Total Submissions: 582.6K
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters char[].
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# You may assume all the characters consist of printable ascii characters.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
# 
# 
# 
#
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s) - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
