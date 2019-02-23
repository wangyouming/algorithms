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
        return self.longestValidParentheses_2(s)
    
    def longestValidParentheses_2(self, s):
        left = right = ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, 2*right)
            elif right >= left:
                left = right = 0
        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, 2*left)
            elif left >= right:
                left = right = 0
        return ans
    
    def longestValidParentheses_1(self, s):
        ans = 0 
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    #dp[i-1]+2+dp[i-dp[i-1]-2]
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1] >= 2 else 0)
                ans = max(ans, dp[i])
        return ans

    def longestValidParentheses_0(self, s):
        ans = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans

if __name__ == '__main__':
    solution = Solution()
    s0 = "(()"
    assert(solution.longestValidParentheses(s0) == 2)
    s1 = ")()())"
    assert(solution.longestValidParentheses(s1) == 4)