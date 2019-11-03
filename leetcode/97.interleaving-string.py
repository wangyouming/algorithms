#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (28.93%)
# Likes:    979
# Dislikes: 55
# Total Accepted:    126.6K
# Total Submissions: 432K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
# 
# Example 1:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        m = {}
        def dp(i: int, j: int) -> bool:
            k = '{}-{}'.format(i, j)
            if k in m: return m[k]

            res = False
            if i == len(s1): res = s3[i+j:] == s2[j:]
            elif j == len(s2): res = s3[i+j:] == s1[i:]
            else:
                res = (s3[i+j] == s1[i] and dp(i+1, j)) or \
                      (s3[i+j] == s2[j] and dp(i, j+1))

            m[k] = res
            return res

        return dp(0, 0)
# @lc code=end
