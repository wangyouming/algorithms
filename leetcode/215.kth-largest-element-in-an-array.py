#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (45.49%)
# Total Accepted:    318.5K
# Total Submissions: 697.3K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        return self.findKthLargest_2(nums, k)
    
    def findKthLargest_2(self, nums, k):
        import heapq
        min_heap = [-float('inf')] * k
        for num in nums:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        return heapq.heappop(min_heap)

    def findKthLargest_1(self, nums, k):
        import heapq
        nums = [-num for num in nums]
        heapq.heapify(nums)
        k -= 1
        for _ in range(k): 
            heapq.heappop(nums)
        return -nums[0]
    
    def findKthLargest_0(self, nums, k):
        nums.sort()
        return nums[-k]
        
