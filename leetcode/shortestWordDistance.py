"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3. Given word1 = "makes", word2 = "coding", return 1.

Note: You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

URL: https://leetcode.com/problems/shortest-word-distance/
"""

class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1, idx2 = -1, -1
        import sys
        dis = sys.maxsize
        for idx, word in enumerate(words):
            if word == word1:
                idx1 = idx
                if idx2 != -1:
                    dis = min(dis, idx1 - idx2)
            elif word == word2:
                idx2 = idx
                if idx1 != -1:
                    dis = min(dis, idx2 - idx1)
        return dis

if __name__ == '__main__':
    solution = Solution()
    assert(solution.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice") == 3) 
    assert(solution.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding") == 1) 