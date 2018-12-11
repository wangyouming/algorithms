"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""
class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit

class SolutionValley:
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i+1] <= prices[i]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i+1] >= prices[i]:
                i += 1
            peak = prices[i]

            max_profit += peak - valley

        return max_profit

class SolutionBruteForce:
    def maxProfit(self, prices):
        memo = {}
        print('begin')
        return self.calculate(prices, 0, memo)

    def calculate(self, prices, s, memo):
        if s >= len(prices): return 0
        if s in memo: return memo[s]
        max = 0
        for i in range(s, len(prices)):
            max_profit = 0
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profit = self.calculate(prices, j + 1, memo) + prices[j] - prices[i]
                    if profit > max_profit:
                        max_profit = profit
            if max_profit > max:
                max = max_profit
        memo[s] = max
        print(memo)
        return max