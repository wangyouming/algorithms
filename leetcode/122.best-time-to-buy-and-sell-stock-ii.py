#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (50.64%)
# Total Accepted:    287.7K
# Total Submissions: 567.3K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit =
# 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 =
# 3.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.maxProfit_1(prices)
        return self.maxProfit_0(prices)

    def maxProfit_0(self, prices):
        if len(prices) <= 1: return 0
        profit = 0
        for i in range(len(prices)):
            profit += max(0, prices[i]-prices[i-1])
        return profit
    
    def maxProfit_1(self, prices):
        states = set()
        states.add((0, False))
        for i in range(len(prices)):
            new_states = set()
            for left, bought in states:
                if bought:
                    left += prices[i]
                    new_states.add((left, False))
                else:
                    left -= prices[i]
                    new_states.add((left, True))
            states.update(new_states)

            max_bought = None
            max_not_bought = None
            for left, bought in states:
                if bought:
                    if max_bought is None or left > max_bought: max_bought = left
                else:
                    if max_not_bought is None or left > max_not_bought: max_not_bought = left
            states = set()
            if max_bought is not None: states.add((max_bought, True))
            if max_not_bought is not None: states.add((max_not_bought, False))
            
        profit = 0
        for left, bought in states:
            if left > profit: profit = left
        return profit
    