class KMP:
    def getNexts(self, pattern: str):
        self.next = [-1] * len(pattern)
        k = -1
        i = 1
        while i < len(pattern):
            while k != -1 and pattern[k + 1] != pattern[i]:
                k = self.next[k]
            if pattern[k + 1] == pattern[i]:
                k += 1
            self.next[i] = k
            i += 1
        
    def index(self, candidate: str, pattern: str):
        self.getNexts(pattern)
        i = 0
        j = 0
        while i < len(candidate):
            while j > 0 and candidate[i] != pattern[j]:
                j = self.next[j - 1] + 1
            if candidate[i] == pattern[j]:
                j += 1
            if j == len(pattern):
                return i - len(pattern) + 1
            i += 1
        return -1

if __name__ == '__main__':
    assert(KMP().index('hello world', 'world') == 'hello world'.index('world'))
        