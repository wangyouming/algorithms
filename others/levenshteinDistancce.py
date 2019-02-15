def levenshtein_distance_bt(word_0: str, word_1: str) -> int:
    import sys
    min_dist = sys.maxsize
    mem = {}
    def _levenshtein_distance_bt(i, j, cur_dist):
        key = "{}-{}".format(i, j)
        if key in mem and cur_dist > mem[key]:
            return
        else:
            mem[key] = cur_dist
        nonlocal min_dist
        if i == len(word_0) or j == len(word_1):
            if i < len(word_0): cur_dist += (len(word_0) - i)
            if j < len(word_1): cur_dist += (len(word_1) - j)
            min_dist = min(min_dist, cur_dist)
            return

        if word_0[i] == word_1[j]:
            _levenshtein_distance_bt(i+1, j+1, cur_dist)
        else:
            _levenshtein_distance_bt(i+1, j, cur_dist+1) # delete a[i] or add before b[j]
            _levenshtein_distance_bt(i, j+1, cur_dist+1) # delete b[j] or add before a[i]
            _levenshtein_distance_bt(i+1, j+1, cur_dist+1) # update a[i] or update b[j]
    _levenshtein_distance_bt(0, 0, 0)
    return min_dist

def levenshtein_distance_dp_fn(word_0: str, word_1: str) -> int:
    #advance from left
    #f(i, j) -> f(i+1, j) f(i, j+1) f(i+1, j+1)
    mem = {}
    def _levenshtein_distance_dp_fn(i: int, j: int) -> int:
        key = '{}-{}'.format(i, j)
        if key in mem: return mem[key]
        if i == len(word_0): return len(word_1)-j
        if j == len(word_1): return len(word_0)-i
        cost = 1 if word_0[i] != word_1[j] else 0
        res = min(_levenshtein_distance_dp_fn(i+1, j)+1, _levenshtein_distance_dp_fn(i, j+1)+1, _levenshtein_distance_dp_fn(i+1, j+1)+cost)
        mem[key] = res
        return res
    return _levenshtein_distance_dp_fn(0, 0)

def levenshtein_distance_dp_matrix(word_0: str, word_1: str) -> int:
    '''
    advance from right
    if a[i] == b[j]:
        min_dist[i][j] = min(min_dist[i-1][j]+1, min_dist[i][j-1])+1, min_dist[i-1][j-1])
    else:
        min_dist[i][j] = min(min_dist[i-1][j], min_dist[i][j-1], min_dist[i-1][j-1]) + 1
    '''
    matrix = [[0] * len(word_1) for _ in range(len(word_0))]
    for i in range(len(word_0)):
        if word_0[i] == word_1[0]: matrix[i][0] = i
        elif i > 0: matrix[i][0] = matrix[i-1][0] + 1
        else: matrix[i][0] = 1
    
    for j in range(len(word_1)):
        if word_0[0] == word_1[j]: matrix[0][j] = j
        elif j > 0: matrix[0][j] = matrix[0][j-1] + 1
        else: matrix[0][j] = 1

    for i in range(1, len(word_0)):
        for j in range(1, len(word_1)):
            if word_0[i] == word_1[j]:
                matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1])
            else:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
    return matrix[-1][-1]

if __name__ == '__main__':
    word_0 = "helloworld"
    word_1 = "takemefaraway"
    print(levenshtein_distance_bt(word_0, word_1))
    print(levenshtein_distance_dp_fn(word_0, word_1))
    print(levenshtein_distance_dp_matrix(word_0, word_1))