#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (31.91%)
# Likes:    1049
# Dislikes: 3264
# Total Accepted:    323.6K
# Total Submissions: 1M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: return s

        rows = [[] for _ in range(numRows)]
        isIncrease = True
        row_num = 0
        for i in range(len(s)):
            row = rows[row_num]
            row.append(s[i])
            if isIncrease:
                row_num += 1
                if row_num == numRows:
                    row_num -= 2
                    isIncrease = False
            else:
                row_num -= 1
                if row_num < 0:
                    row_num += 2
                    isIncrease = True

        rows = ["".join(row) for row in rows]
        return "".join(rows)
