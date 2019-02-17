#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (42.79%)
# Total Accepted:    98.8K
# Total Submissions: 229.7K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
# 
# Example:
# 
# 
# Input: 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output: 
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
# 
# 
#
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #0->2 1->3
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for row in range(i-1, i+2):
                    for col in range(j-1, j+2):
                        if row < 0 or col < 0 or row >= m or col >= n: continue
                        if row == i and col == j: continue
                        if board[row][col] % 2 == 1:
                            live_neighbors += 1
                
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 3
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
