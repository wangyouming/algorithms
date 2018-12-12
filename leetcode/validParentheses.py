"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

URL: https://leetcode.com/problems/valid-parentheses/
"""

from collections import deque

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        q = deque()
        m = {")": "(", "]": "[", "}": "{"}
        for ele in s:
            if ele not in m:
                q.append(ele)
            else:
                v = m[ele]
                if q and q[-1] == v:
                    q.pop()
                else:
                    q.append(ele) 
        return not q