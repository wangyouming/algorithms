"""
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3. Given word1 = "makes", word2 = "coding", return 1.

Note: You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

URL: https://leetcode.com/problems/shortest-word-distance-ii/
"""

class WordDistance:
    def __init__(self, words):
        from collections import defaultdict
        self.m = defaultdict(list)
        for idx, word in enumerate(words):
            self.m[word].append(idx)
    
    def shortest(self, word1, word2):
        indices_1 = self.m[word1] 
        indices_2 = self.m[word2]
        import sys
        res = sys.maxsize
        i = 0
        j = 0
        while i < len(indices_1) and j < len(indices_2):
            if indices_1[i] == indices_2[j]:
                return 0
            elif indices_1[i] > indices_2[j]:
                res = min(res, indices_1[i] - indices_2[j])
                j += 1
            else:
                res = min(res, indices_2[j] - indices_1[i])
                i += 1
        return res

if __name__ == '__main__':
    w = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    assert(w.shortest("coding", "practice") == 3)
    assert(w.shortest("makes", "coding") == 1)