#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (41.76%)
# Likes:    919
# Dislikes: 7285
# Total Accepted:    322.8K
# Total Submissions: 768.6K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0: return ''

        if n == 1: return '1'

        s = self.countAndSay(n-1)
        pre_char = s[0]
        cnt = 1
        ans = ''
        for i in range(1, len(s)):
            if s[i] == pre_char:
                cnt += 1
            else:
                ans += str(cnt)
                ans += pre_char
                cnt = 1
                pre_char = s[i]
        ans += str(cnt)
        ans += pre_char

        return ans
# @lc code=end