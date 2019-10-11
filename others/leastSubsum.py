from typing import List, Mapping

def least_subsum_0(values: List[int], target: int) -> (List[int], int):
    import sys
    min_sum = sys.maxsize
    res_indices = []
    mem = set()
    n = len(values)
    def bt(idx: int, cur_value: int, indices: List[int]):
        nonlocal min_sum, res_indices
        if cur_value >= target or idx == n:
            if cur_value < min_sum and cur_value >= target:
                min_sum = cur_value
                res_indices = indices
            return

        key = '{}-{}'.format(idx, cur_value)
        if key in mem: return
        mem.add(key)
        
        _indices = indices[:]
        _indices.append(idx)
        bt(idx+1, cur_value+values[idx], _indices)
        bt(idx+1, cur_value, indices)

    bt(0, 0, [])

    return (res_indices, min_sum)

def least_subsum_1(values: List[int], target: int) -> (List[int], int):
    nums: Mapping[int, List[int]] = {}
    nums[0] = []
    import sys
    min_num = sys.maxsize
    for idx, value in enumerate(values):
        new_nums: Mapping[int, List[int]] = {}
        for num in nums:
            cur_val = num + value
            if cur_val in nums: continue
            if cur_val in new_nums: continue
            if cur_val >= target:
                if cur_val >= min_num: continue
                else: min_num = cur_val
            indices = nums[num][:]
            indices.append(idx)
            new_nums[cur_val] = indices
        nums.update(new_nums)
    if min_num in nums:
        return nums[min_num], min_num
    else:
        return [], min_num

def least_subsum_2(values: List[int], target: int) -> (List[int], int):
    mem = {}
    def dp(cur_idx: int, target: int) -> (List[int], int):
        key = '{}-{}'.format(cur_idx, target)
        if key in mem: return mem[key]

        if cur_idx == len(values) or target <= 0:
            if target <= 0: return [], 0
            else:
                import sys 
                return [], sys.maxsize

        dp_0 = dp(cur_idx+1, target)
        dp_1 = dp(cur_idx+1, target-values[cur_idx])

        if dp_0[1] < dp_1[1] + values[cur_idx]:
            res = dp_0
        else:
            res = [cur_idx]+dp_1[0], values[cur_idx]+dp_1[1]

        mem[key] = res
        return res

    return dp(0, target)

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 20

    import time

    last = time.time()
    for _ in range(10000):
        res = least_subsum_0(values, target)
    current = time.time()
    print('-'*30)
    print(res)
    print('{:.10f}'.format(current - last))

    last = time.time()
    for _ in range(10000):
        res = least_subsum_1(values, target)
    current = time.time()
    print('-'*30)
    print(res)
    print('{:.10f}'.format(current - last))

    last = time.time()
    for _ in range(10000):
        res = least_subsum_2(values, target)
    current = time.time()
    print('-'*30)
    print(res)
    print('{:.10f}'.format(current - last))