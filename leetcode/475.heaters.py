#
# @lc app=leetcode id=475 lang=python
#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Easy (30.90%)
# Total Accepted:    42.6K
# Total Submissions: 137.8K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! Your first job during the contest is to design a standard
# heater with fixed warm radius to warm all the houses.
# 
# Now, you are given positions of houses and heaters on a horizontal line, find
# out minimum radius of heaters so that all houses could be covered by those
# heaters.
# 
# So, your input will be the positions of houses and heaters seperately, and
# your expected output will be the minimum radius standard of heaters.
# 
# Note:
# 
# 
# Numbers of houses and heaters you are given are non-negative and will not
# exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not
# exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be
# warmed.
# All the heaters follow your radius standard and the warm radius will the
# same.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
#
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        return self.findRadius_1(houses, heaters)
        return self.findRadius_0(houses, heaters)
    
    def findRadius_1(self, houses, heaters):
        def binarySearchNearest(target, values):
            low = 0
            high = len(values) - 1
            while low <= high:
                mid = low + ((high - low) >> 1)
                minus = values[mid] - target
                if minus == 0:
                    return mid
                elif minus > 0:
                    if mid == 0 or values[mid-1]+values[mid] <= 2*target:
                        return mid
                    high = mid-1
                else:
                    if mid == len(values)-1 or values[mid]+values[mid+1] >= 2*target:
                        return mid
                    low = mid+1
            return -1
        radius = 0
        heaters = sorted(heaters)
        for house in houses:
            idx = binarySearchNearest(house, heaters)
            radius = max(radius, abs(house-heaters[idx]))
        return radius
    
    def findRadius_0(self, houses, heaters):
        houses = sorted(houses)
        heaters = sorted(heaters)
        idx = 0
        radius = 0
        for house in houses:
            while idx < len(heaters)-1 and 2*house > heaters[idx] + heaters[idx+1]:
                idx += 1
            radius = max(radius, abs(heaters[idx]-house))
        return radius
