#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (28.71%)
# Total Accepted:    162.6K
# Total Submissions: 560.6K
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# Example 1:
# 
# 
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
#
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChange_0(coins, amount)
    
    def coinChange_0(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            min_cnt = -1
            for coin in coins:
                if i >= coin and dp[i-coin] != -1:
                    if min_cnt == -1 or min_cnt > dp[i-coin]+1:
                        min_cnt = dp[i-coin] + 1
            dp[i] = min_cnt
        return dp[-1]

    def coinChange_1(self, coins: List[int], amount: int) -> int:
        mem = {}
        def dp(amount: int) -> int:
            if amount == 0: return 0
            if amount in mem: return mem[amount]
            min_cnt = -1
            for coin in coins:
                if coin <= amount:
                    left_cnt = dp(amount - coin)
                    if left_cnt != -1 and (min_cnt == -1 or min_cnt > left_cnt + 1):
                        min_cnt = left_cnt + 1
            mem[amount] = min_cnt
            return min_cnt
        return dp(amount)