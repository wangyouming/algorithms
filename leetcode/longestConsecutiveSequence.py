"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

URL: https://leetcode.com/problems/longest-consecutive-sequence/
"""

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.longestConsecutive_0(nums)
        return self.longestConsecutive_1(nums)

    def longestConsecutive_1(self, nums):
        def _longestConsecutive(num, s, step):
            res = 0
            current = num + step
            while current in s:
                s.remove(current)
                current = current + step
                res += 1
            return res
        res = 0
        s = set(nums)
        for num in nums:
            res = max(1 + _longestConsecutive(num, s, -1) + _longestConsecutive(num, s, 1), res)
        return res
    
    def longestConsecutive_0(self, nums):
        s = set(nums)
        res = 0
        for num in nums:
            if num not in s: continue
            s.remove(num)
            current = num - 1
            l = 0
            while current in s:
                s.remove(current)
                current -= 1
                l += 1
            r = 0
            current = num + 1
            while current in s:
                s.remove(current)
                current += 1
                r += 1
            res = max(res, l + r + 1)
        return res 

if __name__ == '__main__':
    assert(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)