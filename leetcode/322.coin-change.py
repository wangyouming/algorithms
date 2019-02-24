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
        mem = {}
        mem[0] = 0
        def dp(target: int) -> int:
            nonlocal mem
            if target in mem: return mem[target]
            if target < 0: return -1
            ans = -1
            for coin in coins:
                cnt = dp(target - coin)
                if cnt != -1 and (ans == -1 or cnt < ans):
                    ans = cnt
            if ans != -1:
                ans += 1
            mem[target] = ans
            return ans
        return dp(amount)

