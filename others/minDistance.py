from typing import List

def min_distance_bt(weights: List[List[int]]) -> int:
    import sys
    min_dist = sys.maxsize
    memo = {}
    m, n = len(weights), len(weights[0])
    def _min_distance_bt(i: int, j: int, cur_dist: int):
        if i >= m or j >= n: return
        
        nonlocal min_dist
        key = '{}-{}'.format(i, j)
        if key in memo and memo[key] < cur_dist:
            return
        else:
            memo[key] = cur_dist

        cur_dist += weights[i][j]
        if i == m-1 and j == n-1:
            min_dist = min(min_dist, cur_dist)
        else:
            _min_distance_bt(i+1, j, cur_dist)
            _min_distance_bt(i, j+1, cur_dist)
        
    _min_distance_bt(0, 0, 0)

    return min_dist

def min_distance_dp_st(weights: List[List[int]]) -> int:
    m, n = len(weights), len(weights[0])
    states = [[0] * n for _ in range(m)]
    sum = 0
    for j in range(n):
        sum += weights[0][j]
        states[0][j] = sum
    
    sum = 0
    for i in range(m):
        sum += weights[i][0]
        states[i][0] = sum
    
    for i in range(1, m):
        for j in range(1, n):
            states[i][j] = min(states[i-1][j], states[i][j-1]) + weights[i][j]
    
    return states[-1][-1]

def min_distance_dp_st_memo(weights: List[List[int]]) -> int:
    m, n = len(weights), len(weights[0])

    last_level = [0] * n
    sum = 0
    for j in range(n):
        sum += weights[0][j]
        last_level[j] = sum
    
    current_level = last_level[:]
    for i in range(1, m):
        current_level[0] = last_level[0] + weights[i][0]
        for j in range(1, n):
            current_level[j] = min(current_level[j-1], last_level[j]) + weights[i][j]
        last_level = current_level[:]

    return current_level[-1]

def min_distance_dp_fn(weights: List[List[int]]) -> int:
    def _min_distance_dp_fn(i, j):
        if i == 0 or j == 0:
            if i == 0 and j == 0:
                return weights[0][0]
            elif i == 0:
                return _min_distance_dp_fn(i, j-1) + weights[i][j]
            else:
                return _min_distance_dp_fn(i-1, j) + weights[i][j]
        else:
            return min(_min_distance_dp_fn(i, j-1), _min_distance_dp_fn(i-1, j)) + weights[i][j]
    return _min_distance_dp_fn(len(weights)-1, len(weights[0])-1) 

if __name__ == '__main__':
    weights = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    print(min_distance_bt(weights))
    print(min_distance_dp_st(weights))
    print(min_distance_dp_st_memo(weights))
    print(min_distance_dp_fn(weights))
