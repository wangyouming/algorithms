#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (40.65%)
# Total Accepted:    187.9K
# Total Submissions: 461.6K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        res = 0
        for num in nums:
            cur_max = 1

            current = num-1
            while current in s:
                cur_max += 1
                s.remove(current)
                current -= 1

            current = num+1
            while current in s:
                cur_max += 1
                s.remove(current)
                current += 1
            
            res = max(res, cur_max)
        
        return res
