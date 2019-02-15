def lcs_bt(word_0: str, word_1: str) -> int:
    lcs = 0
    mem = {}
    def _lcs_bt(i, j, cur_lcs) -> None:
        key = "{}-{}".format(i, j)
        if key in mem and cur_lcs < mem[key]:
            return
        else:
            mem[key] = cur_lcs
        nonlocal lcs
        if i == len(word_0) or j == len(word_1):
            lcs = max(lcs, cur_lcs)
            return

        if word_0[i] == word_1[j]:
            _lcs_bt(i+1, j+1, cur_lcs+1)
        else:
            _lcs_bt(i+1, j, cur_lcs)
            _lcs_bt(i, j+1, cur_lcs)

    _lcs_bt(0, 0, 0)
    return lcs

def lcs_dp_fn(word_0: str, word_1: str) -> int:
    # if a[i] == b[j]: f(i, j) = f(i+1, j+1) + 1
    # else: f(i, j) = max(f(i+1, j), f(i, j+1))
    mem = {}
    def _lcs_dp_fn(i: int, j: int) -> int:
        key = '{}-{}'.format(i, j)
        if key in mem: return mem[key]
        if i >= len(word_0) or j >= len(word_1): return 0
        res = max(_lcs_dp_fn(i+1, j), _lcs_dp_fn(i, j+1)) if word_0[i] != word_1[j] else _lcs_dp_fn(i+1, j+1) + 1
        mem[key] = res
        return res
    return _lcs_dp_fn(0, 0)

def lcs_dp_fn_matrix(word_0: str, word_1: str) -> int:
    # if a[i] == a[j]:
    #     f(i, j) = f(i-1, j-1) + 1
    # else:
    #     f(i, j) = max(f(i-1, j), f(i, j-1))
    matrix = [[0] * len(word_1) for _ in range(len(word_0))]

    for i in range(len(word_0)):
        if word_0[i] == word_1[0]: matrix[i][0] = 1
        elif i > 0: matrix[i][0] = matrix[i-1][0]
        else: matrix[i][0] = 0
    
    for j in range(len(word_1)):
        if word_0[0] == word_1[j]: matrix[0][j] == 1
        elif j > 0: matrix[0][j] = matrix[0][j-1]
        else: matrix[0][j] = 0

    for i in range(1, len(word_0)):
        for j in range(1, len(word_1)):
            if word_0[i] == word_1[j]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[-1][-1]

if __name__ == '__main__':
    word_0 = "hello world"
    word_1 = "take me far away"
    print(lcs_bt(word_0, word_1))
    print(lcs_dp_fn(word_0, word_1))
    print(lcs_dp_fn_matrix(word_0, word_1))