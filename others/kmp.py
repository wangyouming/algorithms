from typing import List

def getNext(pattern: str) -> List[int]:
    next = [-1] * len(pattern)
    k = -1
    i = 1
    while i < len(pattern):
        while k != -1 and pattern[k + 1] != pattern[i]:
            k = next[k]
        if pattern[k + 1] == pattern[i]:
            k += 1
        next[i] = k
        i += 1
    return next
        
def kmp(text: str, pattern: str):
    next = getNext(pattern)
    i = 0
    j = 0
    while i < len(text):
        while j > 0 and text[i] != pattern[j]:
            j = next[j - 1] + 1
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i + 1- len(pattern)
        i += 1
    return -1

if __name__ == '__main__':
    assert(kmp('hello world', 'world') == 'hello world'.index('world'))
        