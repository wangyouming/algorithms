from typing import List

def min_distance_0(matrix: List[List[int]]) -> int:
    import sys
    min_dist = sys.maxsize
    mem = {}
    m, n = len(matrix), len(matrix[0])
    def bt(i: int, j: int, cur_dist: int):
        nonlocal min_dist, mem
        if i >= m or j >= n: return
        key = '{}-{}'.format(i, j)
        if key in mem and cur_dist >= mem[key]:
            return
        else:
            mem[key] = cur_dist
        
        cur_dist += matrix[i][j]
        if i == m-1 and j == n-1:
            min_dist = min(min_dist, cur_dist)
        else:
            bt(i+1, j, cur_dist)
            bt(i, j+1, cur_dist)
    
    bt(0, 0, 0)
    return min_dist

def min_distance_1(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]

    sum = 0
    for j in range(n):
        sum += matrix[0][j]
        dp[0][j] = sum
    
    sum = 0
    for i in range(m):
        sum += matrix[i][0]
        dp[i][0] = sum
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    return dp[-1][-1]

def min_distance_2(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])

    pre_dp = [0] * n
    sum = 0
    for j in range(n):
        sum += matrix[0][j]
        pre_dp[j] = sum
    
    cur_dp = pre_dp[:]
    for i in range(1, m):
        cur_dp[0] = pre_dp[0] + matrix[i][0]
        for j in range(1, n):
            cur_dp[j] = min(cur_dp[j-1], pre_dp[j]) + matrix[i][j]
        pre_dp = cur_dp[:]
    return cur_dp[-1]

def min_distance_3(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    mem = {}
    def dp(i: int, j: int) -> int:
        nonlocal mem
        key = '{}-{}'.format(i, j)
        if key in mem: return mem[key]
        
        if i == 0 or j == 0:
            if i == 0 and j == 0: return matrix[i][j]
            elif i == 0: return dp(i, j-1) + matrix[i][j]
            elif j == 0: return dp(i-1, j) + matrix[i][j]
        else:
            ans = min(dp(i, j-1), dp(i-1, j)) + matrix[i][j]
            mem[key] = ans
            return ans
    return dp(m-1, n-1)

if __name__ == '__main__':
    matrix = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    print(min_distance_0(matrix))
    print(min_distance_1(matrix))
    print(min_distance_2(matrix))
    print(min_distance_3(matrix))
