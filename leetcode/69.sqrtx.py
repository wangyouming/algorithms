#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (30.45%)
# Total Accepted:    327.2K
# Total Submissions: 1.1M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + ((high - low) >> 1)
            product = mid * mid
            if product < x:
                if pow(mid+1, 2) > x:
                    return mid
                low = mid + 1
            elif product > x:
                high = mid - 1
            else:
                return mid
        return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(4))
    print(solution.mySqrt(8))
