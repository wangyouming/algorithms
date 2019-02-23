#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (15.83%)
# Total Accepted:    256.2K
# Total Submissions: 1.6M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string, reverse the string word by word.
# 
# Example:  
# 
# 
# Input: "the sky is blue",
# Output: "blue is sky the".
# 
# 
# Note:
# 
# 
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed
# string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the
# reversed string.
# 
# 
# Follow up: For C programmers, try to solve it in-place in O(1) space.
# 
#
from typing import List

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.reverseWords_1(s)
    
    def reverseWords_1(self, s):
        def strip(l: List[str]) -> int:
            i = 0
            for j in range(len(l)):
                if l[j] == ' ':
                    if i > 0 and j > 0 and l[j-1] != ' ':
                        l[i] = ' '
                        i += 1
                else:
                    l[i] = l[j]
                    i += 1
            for j in range(i, len(l)):
                l[j] = ' '

            if i > 0 and l[i-1] == ' ':
                i -= 1 

            return i
        
        def reverse(l: List[str], i: int, j: int):
            j = j - 1
            while i < j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            
        str_list = list(s)
        str_len = strip(str_list)
        reverse(str_list, 0, str_len)

        i = j = 0
        while j < str_len:
            while i < str_len and str_list[i] == ' ': i += 1
            j = i
            while i < str_len and str_list[j] != ' ': j += 1
            reverse(str_list, i, j)
            i = j

        return ''.join(str_list[:str_len])
    
    def reverseWords_0(self, s):
        return ' '.join(reversed(s.split()))

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords(''))
    assert(solution.reverseWords(" the  sky  is  blue  ") == "blue is sky the")
