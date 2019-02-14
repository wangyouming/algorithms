from typing import List

max_weight = 0
item_weights = [2, 2, 4, 6, 3]
knapsack_capacity = 9

#backtrace solution
def knapsack_max_weight_bt(current_idx: int, current_weight: int):
    global max_weight, item_weights, knapsack_capacity
    if current_weight == knapsack_capacity or current_idx == len(item_weights):
        if current_weight >= max_weight:
            max_weight = current_weight
        return
    
    knapsack_max_weight_bt(current_idx + 1, current_weight)
    if current_weight + item_weights[current_idx] <= knapsack_capacity:
        knapsack_max_weight_bt(current_idx + 1, current_weight + item_weights[current_idx])

#backtrace solution with memory optimization
memo = [[False] * len(item_weights)] * knapsack_capacity
def knapsack_max_weight_bt_memo_opti(current_idx: int, current_weight: int):
    global max_weight, item_weights, knapsack_capacity, memo
    if memo[current_idx][current_weight]: return
    memo[current_idx][current_weight] = True
    if current_weight == knapsack_capacity or current_idx == len(item_weights):
        if current_weight >= max_weight:
            max_weight = current_weight
        return
    
    knapsack_max_weight_bt_memo_opti(current_idx + 1, current_weight)
    if current_weight + item_weights[current_idx] <= knapsack_capacity:
        knapsack_max_weight_bt_memo_opti(current_idx + 1, current_weight + item_weights[current_idx])

#dynamic programming solution: states figure
def knapsack_max_weight_dp(item_weights: List[int], knapsack_capcity: int):
    states = [[False] * (knapsack_capacity + 1)] * len(item_weights)
    states[0][0] = True
    states[0][item_weights[0]] = True
    for i in range(1, len(item_weights)):
        for j in range(knapsack_capacity + 1):
            if states[i-1][j]:
                states[i][j] = True
        for j in range(knapsack_capacity - item_weights[i] + 1):
            if states[i-1][j]:
                states[i][j+item_weights[i]] = True

    for idx, exist in enumerate(reversed(states[-1])):
        if exist:
            return len(states[-1]) - 1 - idx

    return 0

#dynamic programming solution with memory optimization: states figure
def knapsack_max_weight_dp_memo_opti(item_weights: List[int], knapsack_capacity: int):
    states = [False] * (knapsack_capacity + 1)
    states[0] = True
    states[item_weights[0]] = True
    for i in range(1, len(item_weights)):
        #如果j从小到大，会重复
        for j in range(knapsack_capacity - item_weights[i], 0, -1):
            if states[j]:
                states[j + item_weights[i]] = True
    
    for idx, exist in enumerate(reversed(states)):
        if exist:
            return len(states) - 1 - idx
    
    return 0

#dynamic programming: transfer states
def knapsack_max_weight_dp_recur(item_weights: List[int], knapsack_capacity: int):
    #f(idx, w) = max(f(idx-1, w), f(idx-1, w-ws[idx]))
    memo = {}
    def _knapsack_max_weight_dp_recur(idx: int, knapsack_capacity: int):
        key = '{}-{}'.format(idx, knapsack_capacity)
        if key in memo:
            return memo[key]
        if idx == 0:
            if item_weights[idx] > knapsack_capacity: 
                res = 0
            else: 
                res = item_weights[idx]
        else:
            if knapsack_capacity < item_weights[idx]:
                res = _knapsack_max_weight_dp_recur(idx-1, knapsack_capacity)
            else:
                res = max(_knapsack_max_weight_dp_recur(idx-1, knapsack_capacity), _knapsack_max_weight_dp_recur(idx-1, knapsack_capacity- item_weights[idx]) + item_weights[idx])
        memo[key] = res
        return res
    return _knapsack_max_weight_dp_recur(len(item_weights)-1, knapsack_capacity)

max_value = 0
item_weights = [2, 2, 4, 6, 3]
item_values = [3, 4, 8, 9, 6]
knapsack_capacity = 9

def knapsack_max_value_bt(current_idx: int, current_weight: int, current_value: int):
    global max_value, item_weights, item_values, knapsack_capacity
    if current_weight == knapsack_capacity or current_idx == len(item_weights):
        if current_value > max_value:
            max_value = current_value
        return
    knapsack_max_value_bt(current_idx + 1, current_weight, current_value)
    if current_weight + item_weights[current_idx] <= knapsack_capacity:
        knapsack_max_value_bt(current_idx + 1, current_weight + item_weights[current_idx], current_value + item_values[current_idx])

def knapsack_max_value_dp(item_weights: List[int], item_valus: List[int], knapsack_capcity: int):
    states = [[-1] * (knapsack_capacity + 1)] * len(item_weights)
    states[0][0] = 0
    states[0][item_weights[0]] = item_values[0]
    for i in range(1, len(item_weights)):
        for j in range(knapsack_capacity + 1):
            if states[i - 1][j] >= 0:
                states[i][j] = states[i - 1][j]
        for j in range(knapsack_capacity - item_weights[i] + 1):
            if states[i - 1][j] >= 0:
                v = states[i - 1][j] + item_values[i]
                if v > states[i][j + item_weights[i]]:
                    states[i][j + item_weights[i]] = v
    return max(states[-1])

def knapsack_max_value_dp_memo_opti(item_weights: List[int], item_valus: List[int], knapsack_capcity: int):
    states = [-1] * (knapsack_capacity + 1)
    states[0] = 0
    states[item_weights[0]] = item_values[0]
    for i in range(1, len(item_weights)):
        for j in range(knapsack_capacity - item_weights[i], -1, -1):
            v = states[j] + item_values[i]
            if v > states[j + item_weights[i]]:
                states[j + item_weights[i]] = v
    return max(states)

def knapsack_max_value_dp_recur(item_weights: List[int], item_values: List[int], knapsack_capacity: int):
    #f(idx, capacity) = max(f(idx-1, capacity), f(idx-1, capacity-item_weights[idx])+item_values[idx])
    memo = {}
    def _knapsack_max_value_dp_recur(idx: int, knapsack_capacity: int):
        key = '{}-{}'.format(idx, knapsack_capacity)
        if key in memo:
            return memo[key]
        if idx == 0:
            if knapsack_capacity < item_weights[idx]:
                res = 0
            else:
                res = item_values[idx]
        else:
            if knapsack_capacity < item_weights[idx]:
                res = _knapsack_max_value_dp_recur(idx-1, knapsack_capacity)
            else:
                res = max(_knapsack_max_value_dp_recur(idx-1, knapsack_capacity), _knapsack_max_value_dp_recur(idx-1, knapsack_capacity-item_weights[idx])+item_values[idx])
        memo[key] = res
        return res
    return _knapsack_max_value_dp_recur(len(item_weights)-1, knapsack_capacity)

if __name__ == '__main__':
    print(knapsack_max_weight_dp(item_weights, knapsack_capacity))
    print(knapsack_max_weight_dp_memo_opti(item_weights, knapsack_capacity))
    print(knapsack_max_weight_dp_recur(item_weights, knapsack_capacity))

    print(knapsack_max_value_dp(item_weights, item_values, knapsack_capacity))
    print(knapsack_max_value_dp_memo_opti(item_weights, item_values, knapsack_capacity))
    print(knapsack_max_value_dp_recur(item_weights, item_values, knapsack_capacity))