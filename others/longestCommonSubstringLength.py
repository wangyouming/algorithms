def lcs_0(text_0: str, text_1: str) -> int:
    lcs = 0
    mem = {}
    def bt(i, j, cur_lcs) -> None:
        key = "{}-{}".format(i, j)
        if key in mem and cur_lcs <= mem[key]:
            return
        else:
            mem[key] = cur_lcs
        nonlocal lcs
        if i == len(text_0) or j == len(text_1):
            lcs = max(lcs, cur_lcs)
            return

        if text_0[i] == text_1[j]:
            bt(i+1, j+1, cur_lcs+1)
        else:
            bt(i+1, j, cur_lcs)
            bt(i, j+1, cur_lcs)

    bt(0, 0, 0)
    return lcs

def lcs_1(text_0: str, text_1: str) -> int:
    # if a[i] == b[j]: f(i, j) = f(i+1, j+1) + 1
    # else: f(i, j) = max(f(i+1, j), f(i, j+1))
    mem = {}
    def dp(i: int, j: int) -> int:
        key = '{}-{}'.format(i, j)
        if key in mem: return mem[key]
        if i >= len(text_0) or j >= len(text_1): return 0
        res = max(dp(i+1, j), dp(i, j+1)) if text_0[i] != text_1[j] else dp(i+1, j+1) + 1
        mem[key] = res
        return res
    return dp(0, 0)

def lcs_2(text_0: str, text_1: str) -> int:
    # if a[i] == a[j]:
    #     f(i, j) = f(i-1, j-1) + 1
    # else:
    #     f(i, j) = max(f(i-1, j), f(i, j-1))
    dp = [[0] * len(text_1) for _ in range(len(text_0))]

    for i in range(len(text_0)):
        if text_0[i] == text_1[0]: dp[i][0] = 1
        elif i > 0: dp[i][0] = dp[i-1][0]
        else: dp[i][0] = 0
    
    for j in range(len(text_1)):
        if text_0[0] == text_1[j]: dp[0][j] == 1
        elif j > 0: dp[0][j] = dp[0][j-1]
        else: dp[0][j] = 0

    for i in range(1, len(text_0)):
        for j in range(1, len(text_1)):
            if text_0[i] == text_1[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

if __name__ == '__main__':
    text_0 = "hello world"
    text_1 = "take me far away"
    print(lcs_0(text_0, text_1))
    print(lcs_1(text_0, text_1))
    print(lcs_2(text_0, text_1))