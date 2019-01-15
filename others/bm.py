class BM:
    def generateBadCharacter(self, pattern, badCharacter):
        for idx, character in enumerate(pattern):
            ascii = ord(character)
            badCharacter[ascii] = idx

    def generateGoodSuffix(self, pattern, suffix, prefix):
        for i in range(len(pattern)-1):
            j = i
            k = 0
            while (j >= 0 and pattern[j] == pattern[len(pattern) - 1 - k]):
                j -= 1
                k += 1
                suffix[k] = j + 1
            if j == -1: prefix[k] = True
    
    def moveByGoodSuffix(self, j, m, suffix, prefix):
        k = m - 1 - j
        if suffix[k] != -1: return j + 1 - suffix[k]
        for r in range(j+2, m):
            if prefix[m-r] == True:
                return r
        return m

    def indexOf(self, candidate, pattern):
        badCharacter = [-1 for _ in range(256)]
        self.generateBadCharacter(pattern, badCharacter)
        suffix = [-1 for _ in range(len(pattern))]
        prefix = [False for _ in range(len(pattern))]
        self.generateGoodSuffix(pattern, suffix, prefix)
        i = 0
        while i <= len(candidate) - len(pattern):
            j = len(pattern) - 1
            while j >= 0:
                if candidate[i+j] != pattern[j]: break
                j -= 1
            if j < 0: return i
            x = j - badCharacter[ord(candidate[j+i])]
            y = 0
            if j < len(pattern) - 1:
                y = self.moveByGoodSuffix(j, len(pattern), suffix, prefix)
            i = i + max(x, y)

        return -1

if __name__ == '__main__':
    bm = BM()
    idx = bm.indexOf('somehellosome', 'hello')
    print(idx)