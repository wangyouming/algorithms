#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (41.41%)
# Total Accepted:    77.8K
# Total Submissions: 187.4K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
# 
#
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        d = {}
        d[0] = 1
        res = 0
        for num in nums:
            total += num
            if total - k in d:
                res += d[total-k]
            if total in d:
                d[total] = d[total] + 1
            else:
                d[total] = 1
        return res
