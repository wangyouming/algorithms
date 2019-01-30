from collections import deque
from typing import List

class AcNode:
    def __init__(self, char: str):
        self._char = char
        self._children = [None] * 26
        self._is_ending_char = False
        self._length = -1
        self._fail = None

class AhoCorasick:
    def __init__(self):
        self._root = AcNode("/")

    def _build_fail_pointer(self) -> None:
        q = deque()
        q.append(self._root)
        while q:
            node = q.popleft()
            for child in node._children:
                if not child: continue
                if node == self._root:
                    child._fail = self._root
                else:
                    fail = node._fail
                    while fail:
                        fail_child = fail._children[ord(child._char) - ord("a")]
                        if fail_child:
                            child._fail = fail_child
                            break
                        fail = fail._fail
                    if not fail:
                        child._fail = self._root
                q.append(child)
    
    def _insert(self, text: str) -> None:
        node = self._root
        for idx, char in map(lambda x: (ord(x) - ord("a"), x), text):
            if not node._children[idx]:
                node._children[idx] = AcNode(char)
            node = node._children[idx]
        node._is_ending_char = True
        node._length = len(text)

    def insert(self, patterns: List[str]) -> None:
        for pattern in patterns:
            self._insert(pattern)
        self._build_fail_pointer()

    def match(self, text: str) -> None:
        node = self._root
        for i, char in enumerate(text):
            idx = ord(char) - ord("a")
            while not node._children[idx] and node != self._root:
                node = node._fail
            node = node._children[idx]
            if not node:
                node = self._root
            tmp = node
            while tmp != self._root:
                if tmp._is_ending_char:
                    print(f"begin position: {i - tmp._length + 1}, length: {tmp._length}")
                tmp = tmp._fail

if __name__ == '__main__':
    patterns = ["at", "art", "oars", "soar"]
    ac = AhoCorasick()
    ac.insert(patterns)
    ac.match("soarsoars")