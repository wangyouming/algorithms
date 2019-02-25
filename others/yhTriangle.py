from typing import List

def yh_triangle_0(nums: List[List[int]]) -> int:
    mem = {}
    import sys
    min_dis = sys.maxsize
    def bt(i: int, j: int, cur_dis: int) -> None:
        nonlocal min_dis
        key = '{}-{}'.format(i, j)
        if key in mem and cur_dis >= mem[key]:
            return
        else:
            mem[key] = cur_dis
        cur_dis += nums[i][j]
        if i == len(nums) - 1:
            min_dis = min(min_dis, cur_dis)
            return
        bt(i+1, j, cur_dis)
        bt(i+1, j+1, cur_dis)
    bt(0, 0, 0)
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
    for i in range(len(nums)):
        for j in range(i, -1, -1):
            if j == i:
                dp[j] = dp[j-1] + nums[i][j]
            elif j == 0:
                dp[j] = dp[j] + nums[i][j]
            else:
                dp[j] = min(dp[j-1], dp[j]) + nums[i][j]
    return min(dp)

def yh_triangle_3(nums: List[List[int]]) -> int:
    dp = nums[-1][:]
    for i in range(len(nums)-2, -1, -1):
        for j in range(i+1):
            dp[j] = min(dp[j], dp[j+1]) + nums[i][j]
    return dp[0]

def yh_triangle_4(nums: List[List[int]]) -> int:
    mem = {}
    def dp(i: int, j: int) -> int:
        key = '{}-{}'.format(i, j)
        if key in mem:
            return mem[key]
        if i == len(nums) - 1:
            return nums[i][j]
        ans = min(dp(i+1, j), dp(i+1, j+1)) + nums[i][j]
        mem[key] = ans
        return ans
    return dp(0, 0)

if __name__ == '__main__':
    nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
    print(yh_triangle_0(nums))
    print(yh_triangle_1(nums))
    print(yh_triangle_2(nums))
    print(yh_triangle_3(nums))
    print(yh_triangle_4(nums))