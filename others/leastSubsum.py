from typing import List, Tuple, Mapping

IndexValue = Tuple[int, int]

def least_subsum_bt(values: List[int], target: int) -> (List[IndexValue], int):
    import sys
    min_sum = sys.maxsize
    idx_values = []
    mem = set()
    n = len(values)
    def _least_subsum_bt(idx: int, cur_value: int, candidats: List[IndexValue]):
        nonlocal min_sum
        nonlocal idx_values
        if cur_value >= target or idx == n:
            if cur_value < min_sum and cur_value >= target:
                min_sum = cur_value
                idx_values = candidats
            return

        key = '{}-{}'.format(idx, cur_value)
        if key in mem: return
        mem.add(key)
        
        _candidates = candidats[:]
        _candidates.append((idx, values[idx]))
        _least_subsum_bt(idx+1, cur_value+values[idx], _candidates)
        _least_subsum_bt(idx+1, cur_value, candidats)

    _least_subsum_bt(0, 0, [])

    return (idx_values, min_sum)

def least_subsum_dp_st(values: List[int], target: int) -> (List[IndexValue], int):
    nums: Mapping[int, List[int]] = {}
    nums[0] = []
    import sys
    min_num = sys.maxsize
    nums[min_num] = []
    for idx, value in enumerate(values):
        new_nums: Mapping[int, List[int]] = {}
        for num in nums:
            cur_val = num + value
            if cur_val in nums: continue
            if cur_val in new_nums: continue
            if cur_val >= target:
                if cur_val >= min_num: continue
                else: min_num = cur_val
            idx_vals = nums[num][:]
            idx_vals.append((idx, value))
            new_nums[cur_val] = idx_vals
        nums.update(new_nums)
    return (nums[min_num], min_num)

def least_subsum_dp_fn(values: List[int], target: int) -> (List[IndexValue], int):
    #f(idx, val) = min(f(idx+1, val), f(idx+1, val+vals[idx]))
    idx_values = []
    import sys
    min_sum = sys.maxsize
    mem = {}
    n = len(values)
    def _least_subsum_dp_fn(cur_idx: int, cur_sum: int, candidates: List[IndexValue]) -> int:
        nonlocal min_sum
        nonlocal idx_values

        key = '{}-{}'.format(cur_idx, cur_sum)
        if key in mem: return mem[key]

        if cur_sum >= target or cur_idx == n:
            if cur_sum < min_sum and cur_sum >= target:
                min_sum = cur_sum
                idx_values = candidates
            res = cur_sum if cur_sum >= target else sys.maxsize
            mem[key] = res
            return res
        
        _candidates = candidates[:]
        _candidates.append((cur_idx, values[cur_idx]))
        return min(_least_subsum_dp_fn(cur_idx+1, cur_sum, candidates), _least_subsum_dp_fn(cur_idx+1, cur_sum+values[cur_idx], _candidates))

    _least_subsum_dp_fn(0, 0, [])
    return (idx_values, min_sum) 

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 20

    import time

    last = time.time()
    print(least_subsum_bt(values, target))
    current = time.time()
    print('-'*30)
    print('{:.10f}'.format(current - last))

    last = current
    print(least_subsum_dp_st(values, target))
    current = time.time()
    print('-'*30)
    print('{:.10f}'.format(current - last))

    last = current
    print(least_subsum_dp_fn(values, target))
    current = time.time()
    print('-'*30)
    print('{:.10f}'.format(current - last))