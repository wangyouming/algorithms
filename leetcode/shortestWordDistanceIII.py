"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "makes", word2 = "coding", return 1. Given word1 = "makes", word2 = "makes", return 3.

Note: You may assume word1 and word2 are both in the list.

URL: https://leetcode.com/problems/shortest-word-distance-iii/
"""

class Solution:
    def shortestWordDistance(self, words, word1, word2):
        idx1 = -1
        idx2 = -1
        import sys
        res = sys.maxsize
        for idx, word in enumerate(words):
            prev = idx1
            if word == word1:
                idx1 = idx
            if word == word2:
                idx2 = idx
            if idx1 != -1 and idx2 != -1:
                if word1 != word2:
                    res = min(res, abs(idx1 - idx2))
                elif prev != -1 and prev != idx1:
                    res = min(res, idx1 - prev)
        return res

if __name__ == '__main__':
    solution = Solution()
    assert(solution.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding") == 1)
    assert(solution.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes") == 3)