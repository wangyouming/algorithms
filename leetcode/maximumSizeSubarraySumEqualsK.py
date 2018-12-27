"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:

Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:

Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?

URL: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
"""

class Sollution:
    def maxSubarrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        sumToIndex = {}
        sumToIndex[0] = -1
        res = 0
        for idx, num in enumerate(nums):
            sum += num
            if sum - k in sumToIndex:
                res = max(res, idx - sumToIndex[sum - k])
            elif sum not in sumToIndex:
                sumToIndex[sum] = idx
        return res

if __name__ == '__main__':
    assert(Sollution().maxSubarrayLen([1, -1, 5, -2, 3], 3) == 4)
    assert(Sollution().maxSubarrayLen([-2, -1, 2, 1], 1) == 2)