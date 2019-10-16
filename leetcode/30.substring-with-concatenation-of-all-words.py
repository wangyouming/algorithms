#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (24.13%)
# Likes:    642
# Dislikes: 1026
# Total Accepted:    149K
# Total Submissions: 614.5K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []

        from collections import defaultdict
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
        
        m, ans = len(words[0]), []
        for k in range(m):
            left, count, seen = k, 0, defaultdict(int)
            for j in range(k, len(s)-m+1, m):
                word = s[j:j+m]
                if word in counts:
                    seen[word] += 1
                    count += 1
                    while seen[word] > counts[word]:
                        seen[s[left:left+m]] -= 1
                        count -= 1
                        left += m
                    if count == len(words):
                        ans.append(left)
                else:
                    left, count, seen = j+m, 0, defaultdict(int)

        return ans

# @lc code=end