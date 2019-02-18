#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (32.72%)
# Total Accepted:    136.9K
# Total Submissions: 417.5K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
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
        return self.maxProfit_0(prices)
    
    def maxProfit_0(self, prices):
        states = set()
        states.add((0, 0, False))
        for price in prices:
            new_states = set()
            for left, cnt, bought in states:
                if bought:
                    new_states.add((left+price, cnt, False))
                elif cnt < 2:
                    new_states.add((left-price, cnt+1, True))
            states.update(new_states)

            d = {}
            for left, cnt, bought in states:
                key = '{}-{}'.format(cnt, 1 if bought else 0)
                if key not in d or d[key] < left: d[key] = left
            
            states = set()
            for k, v in d.items():
                left = v
                l = k.split('-')
                cnt = int(l[0])
                bought = l[1] == '1'
                states.add((left, cnt, bought))

        profit = 0
        for left, cnt, bought in states:
            profit = max(profit, left)
        return profit
