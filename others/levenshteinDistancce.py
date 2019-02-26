def levenshtein_distance_0(text_0: str, text_1: str) -> int:
    import sys
    min_dist = sys.maxsize
    mem = {}
    def bt(i, j, cur_dist):
        nonlocal min_dist, mem
        key = "{}-{}".format(i, j)
        if key in mem and cur_dist >= mem[key]:
            return
        else:
            mem[key] = cur_dist
        if i == len(text_0) or j == len(text_1):
            if i < len(text_0): cur_dist += (len(text_0) - i)
            if j < len(text_1): cur_dist += (len(text_1) - j)
            min_dist = min(min_dist, cur_dist)
            return

        if text_0[i] == text_1[j]:
            bt(i+1, j+1, cur_dist)
        else:
            bt(i+1, j, cur_dist+1) # delete a[i] or add before b[j]
            bt(i, j+1, cur_dist+1) # delete b[j] or add before a[i]
            bt(i+1, j+1, cur_dist+1) # update a[i] or update b[j]
    bt(0, 0, 0)
    return min_dist

def levenshtein_distance_1(text_0: str, text_1: str) -> int:
    #advance from left
    #f(i, j) -> f(i+1, j) f(i, j+1) f(i+1, j+1)
    mem = {}
    def dp(i: int, j: int) -> int:
        nonlocal mem
        key = '{}-{}'.format(i, j)
        if key in mem: return mem[key]
        if i == len(text_0): return len(text_1)-j
        if j == len(text_1): return len(text_0)-i
        cost = 1 if text_0[i] != text_1[j] else 0
        res = min(dp(i+1, j)+1, dp(i, j+1)+1, dp(i+1, j+1)+cost)
        mem[key] = res
        return res
    return dp(0, 0)

def levenshtein_distance_2(text_0: str, text_1: str) -> int:
    '''
    advance from right
    if a[i] == b[j]:
        min_dist[i][j] = min(min_dist[i-1][j]+1, min_dist[i][j-1])+1, min_dist[i-1][j-1])
    else:
        min_dist[i][j] = min(min_dist[i-1][j], min_dist[i][j-1], min_dist[i-1][j-1]) + 1
    '''
    dp = [[0] * len(text_1) for _ in range(len(text_0))]
    for i in range(len(text_0)):
        if text_0[i] == text_1[0]: dp[i][0] = i
        elif i > 0: dp[i][0] = dp[i-1][0] + 1
        else: dp[i][0] = 1
    
    for j in range(len(text_1)):
        if text_0[0] == text_1[j]: dp[0][j] = j
        elif j > 0: dp[0][j] = dp[0][j-1] + 1
        else: dp[0][j] = 1

    for i in range(1, len(text_0)):
        for j in range(1, len(text_1)):
            if text_0[i] == text_1[j]:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[-1][-1]

if __name__ == '__main__':
    text_0 = "hello world"
    text_1 = "take me far away"
    print(levenshtein_distance_0(text_0, text_1))
    print(levenshtein_distance_1(text_0, text_1))
    print(levenshtein_distance_2(text_0, text_1))