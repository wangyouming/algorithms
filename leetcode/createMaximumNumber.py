"""
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]

URL: https://leetcode.com/problems/create-maximum-number/
"""

class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums1) + len(nums2) < k:
            return [0 for _ in range(k+1)]
        elif len(nums1) + len(nums2) == k:
            return self.mergeTwoArrays(nums1, nums2)
        else:
            res = []
            min_nums1 = k - len(nums2) if k > len(nums2) else 0
            max_nums1 = k if k < len(nums1) else len(nums1)
            for count in range(min_nums1, max_nums1+1):
                currentMax = self.maxNumberInTwoArrays(nums1, count, nums2, k-count)
                if len(currentMax) == len(res) and self.compareTwoArrays(currentMax, 0, res, 0):
                    res = currentMax
                elif len(currentMax) != len(res):
                    res = currentMax
            return res

    def maxNumberInTwoArrays(self, nums1, len1, nums2, len2):
        return self.mergeTwoArrays(self.maxNumberOfArray(nums1, len1), self.maxNumberOfArray(nums2, len2))
    
    def maxNumberOfArray(self, nums, length):
        res = []
        for idx, num in enumerate(nums):
            while res and length-idx+len(res) > length and num > res[-1]:
                res.pop()
            if len(res) < length: res.append(num)

        return res

    def mergeTwoArrays(self, nums1, nums2):
        i, j = 0, 0
        res = []
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                res.append(nums2[j])
                j += 1
            elif j == len(nums2):
                res.append(nums1[i])
                i += 1
            else:
                if self.compareTwoArrays(nums1, i, nums2, j):
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
        return res
    
    def compareTwoArrays(self, nums1, idx1, nums2, idx2):
        i, j = idx1, idx2
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                return True
            elif nums1[i] < nums2[j]:
                return False
            else:
                #相等的时候，不能简单的任选其一,选择后面尽快遇到更大数的
                i += 1
                j += 1
        return j >= len(nums2)
    
if __name__ == '__main__':
    solution = Solution()
    assert(solution.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5) == [9, 8, 6, 5, 3])
    assert(solution.maxNumber([6, 7], [6, 0, 4], 5) == [6, 7, 6, 0, 4])
    assert(solution.maxNumber([3, 9], [8, 9], 3) == [9, 8, 9])
    assert(solution.maxNumber([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15) == [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0])