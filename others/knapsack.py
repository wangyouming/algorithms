from typing import List

def knapsack_weight_0(weights: List[int], capacity: int) -> int:
    mem = set()
    max_weight = 0
    def bt(cur_idx: int, cur_weight: int):
        nonlocal mem, max_weight
        key = '{}-{}'.format(cur_idx, cur_weight)
        if key in mem: return
        mem.add(key)

        if cur_idx == len(weights) or cur_weight == capacity:
            max_weight = max(max_weight, cur_weight)
            return
        bt(cur_idx + 1, cur_weight)
        if cur_weight + weights[cur_idx] <= capacity:
            bt(cur_idx + 1, cur_weight + weights[cur_idx])
    
    bt(0, 0)
    return max_weight

def knapsack_weight_1(weights: List[int], capacity: int):
    dp = [[False] * (capacity + 1)] * len(weights)
    dp[0][0] = True
    if weights[0] <= capacity:
        dp[0][weights[0]] = True

    for i in range(1, len(weights)):
        for j in range(capacity + 1):
            if dp[i-1][j]:
                dp[i][j] = True
        for j in range(capacity - weights[i] + 1):
            if dp[i-1][j]:
                dp[i][j+weights[i]] = True

    for idx in range(capacity, -1, -1):
        if dp[-1][idx]:
            return idx
    return 0

def knapsack_weight_2(weights: List[int], capacity: int):
    dp = [False] * (capacity + 1)
    dp[0] = True
    if weights[0] <= capacity:
        dp[weights[0]] = True

    for i in range(1, len(weights)):
        for j in range(capacity - weights[i], -1, -1):
            if dp[j]:
                dp[j + weights[i]] = True
    
    for idx in range(capacity, -1, -1):
        if dp[idx]:
            return idx
    return 0

def knapsack_weight_3(weights: List[int], capacity: int):
    mem = {}
    def dp(idx: int, capacity: int):
        nonlocal mem
        key = '{}-{}'.format(idx, capacity)
        if key in mem:
            return mem[key]

        res = 0
        if idx == len(weights) - 1:
            res = weights[-1] if weights[-1] <= capacity else 0
        else:
            if weights[idx] <= capacity:
                res = max(dp(idx+1, capacity), dp(idx+1, capacity-weights[idx])+weights[idx])
            else:
                res = dp(idx+1, capacity)
        mem[key] = res
        return res
    return dp(0, capacity)

def knapsack_value_0(weights: List[int], values: List[int], capacity: int) -> int:
    max_value = 0
    mem = {}
    def bt(cur_idx: int, cur_weight: int, cur_value: int):
        nonlocal weights, max_value, mem
        key = '{}-{}'.format(cur_idx, cur_weight)
        if key in mem and cur_value <= mem[key]: return
        else: mem[key] = cur_value

        if cur_weight == capacity or cur_idx == len(weights):
            max_value = max(max_value, cur_value)
            return
        bt(cur_idx + 1, cur_weight, cur_value)
        if cur_weight + weights[cur_idx] <= capacity:
            bt(cur_idx + 1, cur_weight + weights[cur_idx], cur_value + values[cur_idx])
    
    bt(0, 0, 0)
    return max_value

def knapsack_value_1(weights: List[int], values: List[int], capacity: int):
    dp = [[-1] * (capacity + 1)] * len(weights)
    dp[0][0] = 0
    if weights[0] <= capacity: 
        dp[0][weights[0]] = values[0]

    for i in range(1, len(weights)):
        for j in range(capacity + 1):
            if dp[i - 1][j] >= 0:
                dp[i][j] = dp[i - 1][j]
        for j in range(capacity - weights[i] + 1):
            if dp[i - 1][j] >= 0:
                v = dp[i - 1][j] + values[i]
                if v > dp[i][j + weights[i]]:
                    dp[i][j + weights[i]] = v
    return max(dp[-1])

def knapsack_value_2(weights: List[int], values: List[int], capacity: int):
    dp = [-1] * (capacity + 1)
    dp[0] = 0
    if weights[0] <= capacity: 
        dp[weights[0]] = values[0]

    for i in range(1, len(weights)):
        for j in range(capacity - weights[i], -1, -1):
            v = dp[j] + values[i]
            if v > dp[j + weights[i]]:
                dp[j + weights[i]] = v
    return max(dp)

def knapsack_value_3(weights: List[int], values: List[int], capacity: int):
    mem = {}
    def dp(idx: int, capacity: int):
        nonlocal mem
        key = '{}-{}'.format(idx, capacity)
        if key in mem:
            return mem[key]

        res = 0
        if idx == len(weights) - 1:
            res = values[-1] if weights[-1] <= capacity else 0
        else:
            if weights[idx] <= capacity:
                res = max(dp(idx+1, capacity), dp(idx+1, capacity-weights[idx])+values[idx])
            else:
                res = dp(idx+1, capacity)
        mem[key] = res
        return res

    return dp(0, capacity)

if __name__ == '__main__':
    weights = [2, 2, 4, 6, 3]
    values = [3, 4, 8, 9, 6]
    capacity = 9
    print(knapsack_weight_0(weights, capacity))
    print(knapsack_weight_1(weights, capacity))
    print(knapsack_weight_2(weights, capacity))
    print(knapsack_weight_3(weights, capacity))

    print(knapsack_value_0(weights, values, capacity))
    print(knapsack_value_1(weights, values, capacity))
    print(knapsack_value_2(weights, values, capacity))
    print(knapsack_value_3(weights, values, capacity))
