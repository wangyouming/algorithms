#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (32.45%)
# Likes:    833
# Dislikes: 358
# Total Accepted:    157.5K
# Total Submissions: 480.3K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#

# @lc code=start

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restoreIpAddresses_1(s)

    def restoreIpAddresses_1(self, s: str) -> List[str]:
        res = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a + b + c + d == len(s):
                            A = int(s[:a])
                            B = int(s[a:a+b])
                            C = int(s[a+b:a+b+c])
                            D = int(s[a+b+c:a+b+c+d])
                            if A <= 255 and B <= 255 and C <= 255 and D <= 255:
                                t = str(A) + '.' + str(B) + '.' + str(C) + '.' + str(D)
                                if len(t) == len(s) + 3: res.append(t)
        return res
        
    def restoreIpAddresses_0(self, s: str) -> List[str]:
        res = []
        def backtracing(s: str, n: int, out: str) -> None:
            if n == 4:
                if not s: res.append(out)
            else:
                for k in range(1, 4):
                    if len(s) < k: break
                    val = int(s[:k])
                    if val > 255 or len(str(val)) != k: continue
                    backtracing(s[k:], n+1, out+s[:k]+'.' if n < 3 else '')
        backtracing(s, 0, '')
        return res
# @lc code=end