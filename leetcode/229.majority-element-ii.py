#
# @lc app=leetcode id=229 lang=python
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (31.11%)
# Total Accepted:    91.5K
# Total Submissions: 293.7K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_0 = None
        count_0 = 0
        num_1 = None
        count_1 = 0
        for num in nums:
            if num_0 is not None and num_0 == num:
                count_0 += 1
            elif num_1 is not None and num_1 == num:
                count_1 += 1
            elif count_0 == 0:
                num_0 = num
                count_0 = 1
            elif count_1 == 0:
                num_1 = num
                count_1 = 1
            else:
                count_0 -= 1
                count_1 -= 1
        count_0 = 0
        count_1 = 0
        for num in nums:
            if num == num_0:
                count_0 += 1
            elif num == num_1:
                count_1 += 1
        res = []
        if count_0 > len(nums) / 3: res.append(num_0)
        if count_1 > len(nums) / 3: res.append(num_1)
        return res
        
