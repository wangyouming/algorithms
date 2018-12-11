"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

URL: https://leetcode.com/problems/move-zeroes/
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0 #eles in [0..k) are non-zeros
        for idx, num in enumerate(nums):
            if num:
                if k != idx:
                    nums[k], nums[idx] = nums[idx], nums[k]
                k += 1