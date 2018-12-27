"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

URL: https://leetcode.com/problems/majority-element/
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        major = nums[0]
        sum = 0
        for num in nums:
            if num == major:
                sum += 1
            else:
                sum -= 1
            if sum == 0:
                sum = 1
                major = num
        return major
