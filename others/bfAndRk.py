from time import time

def bf(text: str, pattern: str) -> int:
    n = len(text)
    m = len(pattern)
    
    if n <= m:
        return 0 if text == pattern else -1
    
    for i in range(n-m+1):
        for j in range(m):
            if text[i+j] == pattern[j]:
                if j == m - 1:
                    return i
                else:
                    continue
            else:
                break
    return -1

def simple_hash(s: str, start: int, end: str) -> int:
    assert(start < end)
    res = 0
    for c in s[start:end]:
        res += ord(c)
    return res

def rk(text, pattern):
    n = len(text)
    m = len(pattern)

    if n <= m:
        return 0 if pattern == text else -1

    hash_mem = [None] * (n-m+1)
    hash_mem[0] = simple_hash(text, 0, m)
    for i in range(1, n-m+1):
        hash_mem[i] = hash_mem[i-1] - \
                       simple_hash(text, i-1, i) + \
                       simple_hash(text, i+m-1, i+m)
    
    pattern_hash = simple_hash(pattern, 0, m)

    for i, h in enumerate(hash_mem):
        if h == pattern_hash:
            if pattern == text[i:i+m]:
                return i
            else:
                continue
    return -1

if __name__ == '__main__':
    text = 'a'*10000
    pattern = 'a'*200+'b'

    begin = time()
    for _ in range(10):
        res = bf(text, pattern)
    end = time()
    print("[bf] result: {res}, time cost: {time:.5f}".format(res=res, time=end-begin))

    begin = time()
    for _ in range(10):
        res = rk(text, pattern)
    end = time()
    print("[rk] result: {res}, time cost: {time:.5f}".format(res=res, time=end-begin))