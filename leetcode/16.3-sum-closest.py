#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.77%)
# Likes:    1127
# Dislikes: 82
# Total Accepted:    351.9K
# Total Submissions: 768.8K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        from functools import reduce
        closest_sum = reduce(lambda x, y: x + y, nums[:3])
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                else:
                    if abs(closest_sum - target) > abs(s - target):
                        closest_sum = s
                    if s < target: l += 1
                    else: r -= 1
        return closest_sum
