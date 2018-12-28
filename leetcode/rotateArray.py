"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

URL: https://leetcode.com/problems/rotate-array/
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.roate_1(nums, k)

    def roate_1(self, nums, k):
        count = 0
        start = 0
        while count < len(nums):
            prev = nums[start]
            current = start
            while True:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = prev
                prev = temp
                count += 1
                current = next
                if current == start:
                    start += 1
                    break
    
    def rotate_0(self, nums, k):
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        k = k % len(nums)
        reverse(nums, 0, len(nums)-k-1)
        reverse(nums, len(nums)-k, len(nums)-1)
        reverse(nums, 0, len(nums)-1)

if __name__ == '__main__':
   solution = Solution()

   nums = [1,2,3,4,5,6,7]
   solution.rotate(nums, 3)
   assert(nums == [5,6,7,1,2,3,4])

   nums = [-1,-100,3,99]
   solution.rotate(nums, 2)
   assert(nums == [3,99,-1,-100])