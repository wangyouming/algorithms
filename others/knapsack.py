from typing import List

def knapsack_max_weight_bt(weights: List[int], capacity: int) -> int:
    mem = set()
    max_weight = 0
    def _knapsack_max_weight_bt(cur_idx: int, cur_weight: int):
        key = '{}-{}'.format(cur_idx, cur_weight)
        if key in mem: return
        mem.add(key)

        nonlocal max_weight
        if cur_idx == len(weights) or cur_weight == capacity:
            max_weight = max(max_weight, cur_weight)
            return
        _knapsack_max_weight_bt(cur_idx+1, cur_weight)
        if cur_weight+weights[cur_idx] <= capacity:
            _knapsack_max_weight_bt(cur_idx+1, cur_weight+weights[cur_idx])
    
    _knapsack_max_weight_bt(0, 0)
    return max_weight

def knapsack_max_weight_dp_st(weights: List[int], capacity: int):
    states = [[False] * (capacity + 1)] * len(weights)
    states[0][0] = True
    states[0][weights[0]] = True
    for i in range(1, len(weights)):
        for j in range(capacity + 1):
            if states[i-1][j]:
                states[i][j] = True
        for j in range(capacity - weights[i] + 1):
            if states[i-1][j]:
                states[i][j+weights[i]] = True

    for idx in range(capacity, -1, -1):
        if states[-1][idx]:
            return idx
    return 0

def knapsack_max_weight_dp_st_memo(weights: List[int], capacity: int):
    states = [False] * (capacity + 1)
    states[0] = True
    states[weights[0]] = True
    for i in range(1, len(weights)):
        for j in range(capacity - weights[i], 0, -1):
            if states[j]:
                states[j + weights[i]] = True
    
    for idx in range(capacity, -1, -1):
        if states[idx]:
            return idx
    return 0

def knapsack_max_weight_dp_fn(weights: List[int], capacity: int):
    #f(idx, w) = max(f(idx-1, w), f(idx-1, w-ws[idx])+ws[idx])
    mem = {}
    def _knapsack_max_weight_dp_fn(idx: int, capacity: int):
        key = '{}-{}'.format(idx, capacity)
        if key in mem:
            return mem[key]
        if idx == 0:
            if weights[idx] > capacity: 
                res = 0
            else: 
                res = weights[idx]
        else:
            if capacity < weights[idx]:
                res = _knapsack_max_weight_dp_fn(idx-1, capacity)
            else:
                res = max(_knapsack_max_weight_dp_fn(idx-1, capacity), _knapsack_max_weight_dp_fn(idx-1, capacity- weights[idx]) + weights[idx])
        mem[key] = res
        return res
    return _knapsack_max_weight_dp_fn(len(weights)-1, capacity)

def knapsack_max_value_bt(weights: List[int], values: List[int], capacity: int) -> int:
    max_value = 0
    mem = {}
    def _knapsack_max_value_bt(cur_idx: int, cur_weight: int, cur_value: int):
        key = '{}-{}'.format(cur_idx, cur_weight)
        if key in mem and cur_value < mem[key]: return
        else: mem[key] = cur_value

        nonlocal max_value
        if cur_weight == capacity or cur_idx == len(weights):
            max_value = max(max_value, cur_value)
            return
        knapsack_max_value_bt(cur_idx+1, cur_weight, cur_value)
        if cur_weight+weights[cur_idx] <= capacity:
            _knapsack_max_value_bt(cur_idx+1, cur_weight+weights[cur_idx], cur_value+values[cur_idx])
    
    _knapsack_max_value_bt(0, 0, 0)
    return max_value

def knapsack_max_value_dp_st(weights: List[int], valus: List[int], capacity: int):
    states = [[-1] * (capacity + 1)] * len(weights)
    states[0][0] = 0
    states[0][weights[0]] = values[0]
    for i in range(1, len(weights)):
        for j in range(capacity + 1):
            if states[i - 1][j] >= 0:
                states[i][j] = states[i - 1][j]
        for j in range(capacity - weights[i] + 1):
            if states[i - 1][j] >= 0:
                v = states[i - 1][j] + values[i]
                if v > states[i][j + weights[i]]:
                    states[i][j + weights[i]] = v
    return max(states[-1])

def knapsack_max_value_dp_st_memo(weights: List[int], valus: List[int], capacity: int):
    states = [-1] * (capacity + 1)
    states[0] = 0
    states[weights[0]] = values[0]
    for i in range(1, len(weights)):
        for j in range(capacity - weights[i], -1, -1):
            v = states[j] + values[i]
            if v > states[j + weights[i]]:
                states[j + weights[i]] = v
    return max(states)

def knapsack_max_value_dp_fn(weights: List[int], values: List[int], capacity: int):
    #f(idx, capacity) = max(f(idx-1, capacity), f(idx-1, capacity-weights[idx])+values[idx])
    mem = {}
    def _knapsack_max_value_dp_fn(idx: int, capacity: int):
        key = '{}-{}'.format(idx, capacity)
        if key in mem:
            return mem[key]
        if idx == 0:
            if capacity < weights[idx]:
                res = 0
            else:
                res = values[idx]
        else:
            if capacity < weights[idx]:
                res = _knapsack_max_value_dp_fn(idx-1, capacity)
            else:
                res = max(_knapsack_max_value_dp_fn(idx-1, capacity), _knapsack_max_value_dp_fn(idx-1, capacity-weights[idx])+values[idx])
        mem[key] = res
        return res
    return _knapsack_max_value_dp_fn(len(weights)-1, capacity)

if __name__ == '__main__':
    weights = [2, 2, 4, 6, 3]
    values = [3, 4, 8, 9, 6]
    capacity = 9
    print(knapsack_max_weight_bt(weights, capacity))
    print(knapsack_max_weight_dp_st(weights, capacity))
    print(knapsack_max_weight_dp_st_memo(weights, capacity))
    print(knapsack_max_weight_dp_fn(weights, capacity))

    print(knapsack_max_value_dp_st(weights, values, capacity))
    print(knapsack_max_value_dp_st_memo(weights, values, capacity))
    print(knapsack_max_value_dp_fn(weights, values, capacity))