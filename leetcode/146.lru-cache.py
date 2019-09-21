#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (27.35%)
# Likes:    3585
# Dislikes: 144
# Total Accepted:    351.2K
# Total Submissions: 1.3M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}

    def _erase(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _insert(self, node):
        self.head.next.prev, self.head.next, node.prev, node.next = \
            node, node, self.head, self.head.next

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        node = self.dict[key]

        self._erase(node)
        self._insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self._erase(node)
            self._insert(node)
        else:
            if len(self.dict) == self.capacity:
                node = self.tail.prev
                self._erase(node)
                del self.dict[node.key]
            node = Node(key, value)
            self._insert(node)
            self.dict[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
