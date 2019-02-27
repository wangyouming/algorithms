#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (26.06%)
# Total Accepted:    761.7K
# Total Submissions: 2.9M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.lengthOfLongestSubstring_1(s)

    def lengthOfLongestSubstring_1(self, s):
        m = {}
        i = j = 0
        ans = 0
        while j < len(s):
            if s[j] in m:
                i = max(i, m[s[j]]+1)
            ans = max(ans, j - i + 1)
            m[s[j]] = j
            j += 1
        return ans

    def lengthOfLongestSubstring_0(self, s):
        m = set()
        i = j =0
        ans = 0
        while i < len(s) and j < len(s):
            if s[j] not in m:
                m.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                m.remove(s[i])
                i += 1
        return ans
