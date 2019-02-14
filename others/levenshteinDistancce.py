def levenshtein_distance_bt(word_0: str, world_1: str) -> int:
    import sys
    min_dist = sys.maxsize
    memo = {}
    def _levenshtein_distance_bt(i, j, cur_dist):
        key = "{}-{}".format(i, j)
        if key in memo and cur_dist > memo[key]:
            return
        else:
            memo[key] = cur_dist
        nonlocal min_dist
        if i == len(word_0) or j == len(world_1):
            if i < len(word_0): cur_dist += (len(word_0) - i)
            if j < len(world_1): cur_dist += (len(world_1) - j)
            min_dist = min(min_dist, cur_dist)
            return

        if word_0[i] == world_1[j]:
            _levenshtein_distance_bt(i+1, j+1, cur_dist)
        else:
            _levenshtein_distance_bt(i+1, j, cur_dist+1) # delete a[i] or add before b[j]
            _levenshtein_distance_bt(i, j+1, cur_dist+1) # delete b[j] or add before a[i]
            _levenshtein_distance_bt(i+1, j+1, cur_dist+1) # update a[i] or update b[j]
    _levenshtein_distance_bt(0, 0, 0)
    return min_dist

def levenshtein_distance_dp_fn(word_0: str, word_1: str) -> int:
    '''
    (i-1, j, dist) -- +(1, 0, 1) ---> (i, j, dist+1)
    (i, j-1, dist) -- +(0, 1, 1) ---> (i, j, dist+1)
    (i-1, j-1, dist) -- +(1, 1, 1)/+(1, 1, 0) ---> (i, j, dist+1)/(i, j, dist)

    if a[i] != b[j]:
        min_dist(i, j) = min(min_dist(i-1, j)+1, min_dist(i, j-1)+1, min_dist(i-1, j-1)+1)
    else:
        min_dist(i, j) == min(min_dist(i-1, j)+1, min_dist(i, j-1)+1, min_dist(i-1, j-1))
    '''
    min_dist_matrix = [[0] * len(word_1) for _ in range(len(word_0))]
    for j in range(len(word_1)):
        if word_0[0] == word_1[j]: min_dist_matrix[0][j] = j
        elif j != 0: min_dist_matrix[0][j] = min_dist_matrix[0][j-1]+1
        else: min_dist_matrix[0][j] = 1
    for i in range(len(word_0)):
        if word_0[i] == word_1[0]: min_dist_matrix[i][0] = i
        elif i != 0: min_dist_matrix[i][0] = min_dist_matrix[i-1][0]+1
        else: min_dist_matrix[i][0] = 1
    
    for i in range(1, len(word_0)):
        for j in range(1, len(word_1)):
            if word_0[i] == word_1[j]:
                min_dist_matrix[i][j] = min(min_dist_matrix[i-1][j]+1, min_dist_matrix[i][j-1]+1, min_dist_matrix[i-1][j-1])
            else:
                min_dist_matrix[i][j] = min(min_dist_matrix[i-1][j]+1, min_dist_matrix[i][j-1]+1,min_dist_matrix[i-1][j-1]+1)
    return min_dist_matrix[-1][-1]

if __name__ == '__main__':
    word_0 = "helloworld"
    word_1 = "takemefaraway"
    print(levenshtein_distance_bt(word_0, word_1))
    print(levenshtein_distance_dp_fn(word_0, word_1))