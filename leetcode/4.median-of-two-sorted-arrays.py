#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (26.40%)
# Likes:    4338
# Dislikes: 581
# Total Accepted:    439.1K
# Total Submissions: 1.7M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.findMedianSortedArrays_1(nums1, nums2)

    def findMedianSortedArrays_1(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(nums1: List[int], i: int, nums2: List[int], j: int, k: int) -> int:
            if i >= len(nums1): return nums2[j+k-1]
            if j >= len(nums2): return nums1[i+k-1]
            if k == 1: return min(nums1[i], nums2[j])
            import sys
            x = nums1[i+k//2-1] if i+k//2-1 < len(nums1) else sys.maxsize
            y = nums2[j+k//2-1] if j+k//2-1 < len(nums2) else sys.maxsize
            if x < y: return findKth(nums1, i+k//2, nums2, j, k-k//2)
            else: return findKth(nums1, i, nums2, j+k//2, k-k//2)
    
        m, n = len(nums1), len(nums2)
        left, right = (m + n + 1) // 2, (m + n + 2) //2
        return (findKth(nums1, 0, nums2, 0, left)+findKth(nums1, 0, nums2, 0, right)) * 0.5

    def findMedianSortedArrays_0(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if n == 0: return 0
        
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    return float(max_of_left)
                
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2
