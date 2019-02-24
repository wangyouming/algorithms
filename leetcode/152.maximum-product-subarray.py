#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (28.39%)
# Total Accepted:    188.7K
# Total Submissions: 662.5K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = big = small = nums[0]
        for num in nums[1:]:
            big, small = max(num, num*big, num*small), min(num, num*big, num*small)
            max_num = max(max_num, big)
        return max_num
