#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (52.90%)
# Total Accepted:    335.7K
# Total Submissions: 631.4K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute_0(nums)

    def permute_1(self, nums):
        perms = [[]]
        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perms.append(perm[:i]+[num]+perm[i:])
            perms = new_perms
        return perms
    
    def permute_0(self, nums):
        res = []
        def backtrace(cur_nums):
            if len(cur_nums) == len(nums):
                res.append(cur_nums[:])
                return
            for i in range(len(nums)):
                if nums[i] in cur_nums: continue
                cur_nums.append(nums[i])
                backtrace(cur_nums)
                cur_nums.pop()
        backtrace([])
        return res
