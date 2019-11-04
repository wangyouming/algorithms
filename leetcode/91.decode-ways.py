#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (22.90%)
# Likes:    1815
# Dislikes: 2050
# Total Accepted:    309.8K
# Total Submissions: 1.3M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        return self.numDecodings_1(s)

    def numDecodings_1(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        prepre, pre = 1, 1
        for i in range(1, len(s)):
            temp = pre
            if s[i] == '0': pre = 0
            if s[i-1] == '1' or (s[i-1] == '2' and int(s[i]) <= 6):
                pre += prepre
            prepre = temp
        return pre 

    def numDecodings_0(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i-1] != '0': dp[i] = dp[i-1]
            if i > 1 and (s[i-2] == '1' or (s[i-2] == '2' and int(s[i-1]) <= 6)):
                dp[i] += dp[i-2]
        return dp[-1]
# @lc code=end