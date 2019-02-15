#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (51.19%)
# Total Accepted:    342.9K
# Total Submissions: 668.9K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        count = 0
        majority = nums[0] 
        for num in nums:
            if num == majority: count += 1
            else: count -= 1
            if count == 0:
                majority = num
                count = 1
        return majority
