#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (41.18%)
# Likes:    1582
# Dislikes: 205
# Total Accepted:    467.1K
# Total Submissions: 1.1M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#

# @lc code=start

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = self.searchFirstEqualOrGreater(nums, target)
        return idx if idx != -1 else len(nums)

    def searchFirstEqualOrGreater(self, nums: List[int], target: int):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            if nums[mid] >= target:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                else:
                    hi = hi - 1
            else:
                lo = mid + 1
        return -1
        
# @lc code=end