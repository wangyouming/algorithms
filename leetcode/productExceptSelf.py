"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

URL: https://leetcode.com/problems/product-of-array-except-self/ 
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for _ in range(len(nums))]
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in reversed(range(len(nums))):
            res[i] = res[i] * right
            right = nums[i] * right
        return res

if __name__ == '__main__':
    assert(Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])