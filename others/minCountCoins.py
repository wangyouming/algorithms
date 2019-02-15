from typing import List

def min_count_coins_bt(values: List[int], target: int) -> int:
    values = sorted(values)[::-1]
    import sys
    min_count = sys.maxsize
    mem = {}
    def _min_count_coins_bt(cur_cnt, left):
        if left in mem and cur_cnt > mem[left]:
            return
        mem[left] = cur_cnt

        nonlocal min_count
        if left == 0:
            min_count = min(min_count, cur_cnt)
            return

        for value in values:
            if value <= left:
                _min_count_coins_bt(cur_cnt+1, left - value)
    _min_count_coins_bt(0, target)

    return min_count

def min_count_coins_dp_st(values: List[int], target: int) -> int:
    mem = [0] * (target+1)
    for i in range(1, target+1):
        import sys
        min_num = sys.maxsize
        for value in values:
            if i >= value:
                min_num = min(min_num, mem[i-value]+1)
        mem[i] = min_num
    return mem[-1]

def min_count_coins_dp_fn(values: List[int], target: int) -> int:
    # f(target) = min(f(target-value0), f(target-value1), ...)
    mem = {}
    def _min_count_coins_dp_fn(target: int) -> int:
        if target == 0: return 0
        if target in mem: return mem[target]
        _values = list(filter(lambda x: x <= target, values))
        import sys
        min_count = sys.maxsize
        for value in _values:
            min_count = min(min_count, _min_count_coins_dp_fn(target - value))
        res = min_count + 1
        mem[target] = res
        return res
    
    return _min_count_coins_dp_fn(target)

if __name__ == '__main__':
    target = 23
    values = [1, 3, 5]
    print(min_count_coins_bt(values, target))
    print(min_count_coins_dp_st(values, target))
    print(min_count_coins_dp_fn(values, target))