#
# @lc app=leetcode id=10 lang=python
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (24.85%)
# Total Accepted:    274K
# Total Submissions: 1.1M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
# 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
# 
# 
#
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.isMatch_0(s, p)

    def isMatch_2(self, text, pattern):
        dp = [[False] * (len(pattern) +1) for _ in range(len(text)+1)]
        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern)-1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
    
    def isMatch_1(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) in memo: return memo[i, j]
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or (first_match and dp(i+1, j))
                else:
                    ans = first_match and dp(i+1, j+1)
            memo[i, j] = ans
            return ans
        return dp(0, 0)
    
    def isMatch_0(self, text, pattern):
        if not pattern: return not text
        
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':
            return self.isMatch_1(text, pattern[2:]) or (first_match and self.isMatch_1(text[1:], pattern))
        else:
            return first_match and self.isMatch_1(text[1:], pattern[1:])

if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch("aa", "a"))
    print(solution.isMatch("aa", "a*"))
    print(solution.isMatch("ab", ".*"))
    print(solution.isMatch("aab", "c*a*b"))
    print(solution.isMatch("mississippi", "mis*is*p*"))
        
