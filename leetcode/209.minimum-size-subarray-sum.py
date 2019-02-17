#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (34.08%)
# Total Accepted:    160.6K
# Total Submissions: 470.5K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s: return 0
        begin = 0
        end = 0
        total = 0
        res = len(nums) 
        while end < len(nums):
            total += nums[end]
            if total >= s:
                res = min(res, end-begin+1)
                while True:
                    total -= nums[begin]
                    begin += 1
                    if total >= s:
                        res = min(res, end-begin+1)
                    else:
                        break
            end += 1
        return res
