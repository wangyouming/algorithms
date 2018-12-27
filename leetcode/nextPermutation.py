"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

URL: https://leetcode.com/problems/next-permutation/
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        while nums[right] <= nums[right-1] and right > 0:
            right -= 1
        if right == 0:
            nums.reverse()
        else:
            pivot = right - 1
            right = len(nums) - 1
            while nums[right] <= nums[pivot]:
                right -= 1
            nums[pivot], nums[right] = nums[right], nums[pivot]
            self.reverse(nums, pivot+1, len(nums)-1)
    
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

if __name__ == '__main__':
    solution = Solution()

    origin = [1, 2, 3]
    solution.nextPermutation(origin)
    assert(origin == [1, 3, 2])

    origin = [3, 2, 1]
    solution.nextPermutation(origin)
    assert(origin == [1, 2, 3])

    origin = [1, 1, 5]
    solution.nextPermutation(origin)
    assert(origin == [1, 5, 1])

    origin = [1, 3, 2]
    solution.nextPermutation(origin)
    assert(origin == [2, 1, 3])