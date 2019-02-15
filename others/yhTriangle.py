from typing import List

def yh_triangle_bt(nums: List[List[int]]) -> int:
    memo = {}
    import sys
    min_dis = sys.maxsize
    def _yh_triangle_bt(row: int, col: int, cur_dis: int) -> None:
        nonlocal min_dis
        key = '{}-{}'.format(row, col)
        if key in memo and cur_dis > memo[key]:
            return
        else:
            memo[key] = cur_dis
        
        cur_dis += nums[row][col]
        if row == len(nums) - 1:
            min_dis = min(min_dis, cur_dis)
            return
        _yh_triangle_bt(row+1, col, cur_dis)
        _yh_triangle_bt(row+1, col+1, cur_dis)
    
    _yh_triangle_bt(0, 0, 0)
    return min_dis

def yh_triangle_dp_st(nums: List[List[int]]) -> int:
    states = [[0] * len(nums) for _ in range(len(nums))]
    states[0][0] = nums[0][0]
    for i in range(1, len(nums)):
        for j in range(i+1):
            if j == 0:
                states[i][j] = states[i-1][j] + nums[i][j]
            elif j == i:
                states[i][j] = states[i-1][j-1] + nums[i][j]
            else:
                states[i][j] = min(states[i-1][j-1], states[i-1][j]) + nums[i][j]
    return min(states[-1])

def yh_triangle_dp_st_memo(nums: List[List[int]]) -> int:
    states = [0] * len(nums)
    states[0] = nums[0][0]
    for i in range(1, len(nums)):
        for j in range(i, -1, -1):
            if j == i:
                states[j] = states[j-1]+nums[i][j]
            elif j == 0:
                states[j] = states[j] + nums[j][j]
            else:
                states[j] = min(states[j-1], states[j]) + nums[i][j]
    return min(states)

def yh_triangle_dp_bottom_up(nums: List[List[int]]) -> int:
    n = len(nums)
    states = nums[-1][:]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            states[j] = min(states[j], states[j+1]) + nums[i][j]
    return states[0]

if __name__ == '__main__':
    nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
    print(yh_triangle_bt(nums))
    print(yh_triangle_dp_st(nums))
    print(yh_triangle_dp_st_memo(nums))
    print(yh_triangle_dp_bottom_up(nums))