from time import time

def bf(text, pattern):
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

def simple_hash(s,start, end):
    assert(start <= end)
    res = 0
    for c in s[start:end+1]:
        res += ord(c)
    return res

def rk(text, pattern):
    n = len(text)
    m = len(pattern)

    if n <= m:
        return 0 if pattern == text else -1

    hash_memo = [None] * (n-m+1)
    hash_memo[0] = simple_hash(text, 0, m-1)
    for i in range(1, n-m+1):
        hash_memo[i] = hash_memo[i-1] - simple_hash(text, i-1, i-1) + simple_hash(text, i+m-1, i+m-1)
    
    hash_p = simple_hash(pattern, 0, m-1)

    for i, h in enumerate(hash_memo):
        if h == hash_p:
            if pattern == text[i:i+m]:
                return i
            else:
                continue
    return -1

if __name__ == '__main__':
    m_str = 'a'*10000
    p_str = 'a'*200+'b'

    print('--- time consume ---')
    t = time()
    print('[bf] result:', bf(m_str, p_str))
    print('[bf] time cost: {0:.5}s'.format(time()-t))

    t = time()
    print('[rk] result:', rk(m_str, p_str))
    print('[rk] time cost: {0:.5}s'.format(time()-t))

    print('')
    print('--- search ---')
    m_str = 'thequickbrownfoxjumpsoverthelazydog'
    p_str = 'jump'
    print('[bf] result:', bf(m_str, p_str))
    print('[rk] result:', rk(m_str, p_str))