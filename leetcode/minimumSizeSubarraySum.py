"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

URL: https://leetcode.com/problems/minimum-size-subarray-sum/
"""
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = -1
        sum = 0
        l = len(nums) + 1
        while left < len(nums):
            if right + 1 < len(nums) and sum < s:
                right += 1
                sum += nums[right]
            else:
                sum -= nums[left]
                left += 1
            if sum >= s:
                l = min(l, right - left + 1)
        return l if l <= len(nums) else 0

print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))