from typing import List

def yh_triangle_0(nums: List[List[int]]) -> int:
    memo = {}
    import sys
    min_dis = sys.maxsize
    def yh_triangle(row: int, col: int, cur_dis: int) -> None:
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
        yh_triangle(row+1, col, cur_dis)
        yh_triangle(row+1, col+1, cur_dis)
    
    yh_triangle(0, 0, 0)
    return min_dis

def yh_triangle_1(nums: List[List[int]]) -> int:
    dp = [[0] * len(nums) for _ in range(len(nums))]
    dp[0][0] = nums[0][0]
    for i in range(1, len(nums)):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + nums[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + nums[i][j]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + nums[i][j]
    return min(dp[-1])

def yh_triangle_2(nums: List[List[int]]) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0][0]
    for i in range(1, len(nums)):
        for j in range(i, -1, -1):
            if j == i:
                dp[j] = dp[j-1]+nums[i][j]
            elif j == 0:
                dp[j] = dp[j] + nums[j][j]
            else:
                dp[j] = min(dp[j-1], dp[j]) + nums[i][j]
    return min(dp)

def yh_triangle_3(nums: List[List[int]]) -> int:
    n = len(nums)
    dp = nums[-1][:]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[j] = min(dp[j], dp[j+1]) + nums[i][j]
    return dp[0]

if __name__ == '__main__':
    nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
    print(yh_triangle_0(nums))
    print(yh_triangle_1(nums))
    print(yh_triangle_2(nums))
    print(yh_triangle_3(nums))