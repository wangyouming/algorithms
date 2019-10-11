from typing import List, Tuple

def generateBadCharacters(pattern: str) -> List[int]:
    bc = [-1 for _ in range(256)]
    for idx, char in enumerate(pattern):
        ascii = ord(char)
        bc[ascii] = idx
    return bc

def generateGoodSuffix(pattern: str) -> Tuple[List[int], List[bool]]:
    suffix = [-1 for _ in range(len(pattern))]
    prefix = [False for _ in range(len(pattern))]
    for i in range(len(pattern)-1):
        j = i
        k = 0
        while (j >= 0 and pattern[j] == pattern[len(pattern) - 1 - k]):
            k += 1
            suffix[k] = j
            j -= 1
        if j == -1: prefix[k] = True
    return suffix, prefix

def moveByGoodSuffix(bad_idx: int, pattern_len: int, \
                     suffix: List[int], prefix: List[bool]) -> int:
    k = pattern_len - 1 - bad_idx
    if suffix[k] != -1: return bad_idx + 1 - suffix[k]
    for begin in range(bad_idx+2, pattern_len):
        if prefix[pattern_len-begin] == True:
            return begin
    return pattern_len

def bm(text: str, pattern: str) -> int:
    bc = generateBadCharacters(pattern)
    suffix, prefix = generateGoodSuffix(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0:
            if text[i+j] != pattern[j]: break
            j -= 1
        if j < 0: return i
        x = j - bc[ord(text[i+j])]
        y = 0
        if j < len(pattern) - 1:
            y = moveByGoodSuffix(j, len(pattern), suffix, prefix)
        i = i + max(x, y)

    return -1

if __name__ == '__main__':
    print(bm('hello world', 'world'))