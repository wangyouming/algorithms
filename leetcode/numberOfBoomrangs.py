"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

URL: https://leetcode.com/problems/number-of-boomerangs/
"""

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for i in range(len(points)):
            record = {}
            for j in range(len(points)):
                if i == j: continue
                dis = self.dis([points[i], points[j]])
                if dis not in record:
                    record[dis] = 1
                else:
                    record[dis] += 1
            for count in record.values():
                if count <= 1: continue
                else:
                    cnt += count*(count - 1)
        return cnt

    def dis(self, points):
        return pow(points[0][0] - points[1][0], 2) + pow(points[0][1] - points[1][1], 2)

print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))
                    