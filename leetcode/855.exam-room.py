#
# @lc app=leetcode id=855 lang=python
#
# [855] Exam Room
#
# https://leetcode.com/problems/exam-room/description/
#
# algorithms
# Medium (36.69%)
# Total Accepted:    11.4K
# Total Submissions: 31.2K
# Testcase Example:  '["ExamRoom","seat","seat","seat","seat","leave","seat"]\n[[10],[],[],[],[],[4],[]]'
#
# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ...,
# N-1.
# 
# When a student enters the room, they must sit in the seat that maximizes the
# distance to the closest person.  If there are multiple such seats, they sit
# in the seat with the lowest number.  (Also, if no one is in the room, then
# the student sits at seat number 0.)
# 
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat()
# returning an int representing what seat the student sat in, and
# ExamRoom.leave(int p) representing that the student in seat number p now
# leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a
# student sitting in seat p.
# 
# 
# 
# Example 1:
# 
# 
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"],
# [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
# 
# 
# ​​​​​​​
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across
# all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting
# in seat number p.
# 
# 
#
class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.n = N
        self.students = []

    def seat(self):
        """
        :rtype: int
        """
        position = 0
        max_dis = 0
        for i in range(1, len(self.students)):
            dis = (self.students[i] - self.students[i-1]) / 2
            if dis > max_dis:
                max_dis = dis
                position = self.students[i-1] + dis

        if not self.students:
            position = 0
        else:
            if self.students[0] != 0 and self.students[0] >= max_dis:
                max_dis = self.students[0]
                position = 0
            if self.students[-1] != self.n-1 and self.n-1-self.students[-1] > max_dis:
                position = self.n-1

        self.students.append(position)
        self.students = sorted(self.students)
        return position

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.students.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
