#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (30.67%)
# Likes:    1084
# Dislikes: 218
# Total Accepted:    237.7K
# Total Submissions: 775K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.fourSum_1(nums, target)
    
    def fourSum_1(self, nums: List[int], target: int) -> List[List[int]]:
        def nSum(l: int, r: int, target: int, N: int, result: List[int], results: List[List[int]]):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
                return
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r + 1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        nSum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)
        nums.sort()
        results = []
        nSum(0, len(nums)-1, target, 4, [], results)
        return results
    
    def fourSum_0(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 4: return res
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]: continue
            threeSum = target - nums[i]

            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                
                twoSum = threeSum - nums[j]

                l, r = j + 1, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s > twoSum:
                        r -= 1
                    elif s < twoSum:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]: l += 1
                        while l < r and nums[r] == nums[r-1]: r -= 1
                        l += 1
                        r -= 1
        return res
