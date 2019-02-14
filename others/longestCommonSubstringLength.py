def longest_common_substring_length_bt(word_0: str, word_1: str) -> int:
    lcs = 0
    memo = {}
    def _longest_common_substring_length_bt(i, j, cur_lcs) -> None:
        key = "{}-{}".format(i, j)
        if key in memo and cur_lcs < memo[key]:
            return
        else:
            memo[key] = cur_lcs
        nonlocal lcs
        if i == len(word_0) or j == len(word_1):
            lcs = max(lcs, cur_lcs)
            return

        if word_0[i] == word_1[j]:
            _longest_common_substring_length_bt(i+1, j+1, cur_lcs+1)
        else:
            _longest_common_substring_length_bt(i+1, j, cur_lcs)
            _longest_common_substring_length_bt(i, j+1, cur_lcs)

    _longest_common_substring_length_bt(0, 0, 0)
    return lcs

def longest_common_substring_length_dp_fn(word_0: str, word_1: str) -> int:
    '''
    (i-1, j, lcs) -- +(1, 0, 0) --> (i, j, lcs)
    (i, j-1, lcs) -- +(0, 1, 0) --> (i, j, lcs)
    (i-1, j-1, lcs) -- +(1, 1, 1) --> (i, j, lcs+1)

    if a[i] == a[j]:
        lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], lcs[i-1][j-1]+1)
    else:
        lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    '''
    lcs_matrix = [[0] * len(word_1) for _ in range(len(word_0))]

    for j in  range(len(word_1)):
        if word_0[0] == word_1[j]: lcs_matrix[0][j] = 1
        elif j > 0: lcs_matrix[0][j] = lcs_matrix[0][j-1]

    for i in range(len(word_0)):
        if word_0[i] == word_1[0]: lcs_matrix[i][0] = 1
        elif i > 0: lcs_matrix[i][0] = lcs_matrix[i-1][0]

    for i in range(1, len(word_0)):
        for j in range(1, len(word_1)):
            if word_0[i] == word_1[j]:
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1], lcs_matrix[i-1][j-1]+1)
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])
    return lcs_matrix[-1][-1]

if __name__ == '__main__':
    word_0 = "helloworld"
    word_1 = "takemefaraway"
    print(longest_common_substring_length_bt(word_0, word_1))
    print(longest_common_substring_length_dp_fn(word_0, word_1))