from typing import Optional
from queue import Queue
import math

class TreeNode:
    def __init__(self, value=None):
        self._value = value
        self._left: Optional[TreeNode] = None
        self._right: Optional[TreeNode] = None
        self._parent: Optional[TreeNode] = None

class BinarySearchTree:
    def __init__(self, values=[]):
        self._root: Optional[TreeNode] = None
        for value in values:
            self.insert(value)

    def insert(self, value):
        if not self._root:
            self._root = TreeNode(value)
        else:
            node = self._root
            parent = node
            while node:
                parent = node
                if value < node._value:
                    node = node._left
                else:
                    node = node._right
            
            new_node = TreeNode(value)
            new_node._parent = parent
            if value < parent._value:
                parent._left = new_node
            else:
                parent._right = new_node

    def search(self, value):
        res = []
        node = self._root
        while node:
            if value < node._value:
                node = node._left
            else:
                if value == node._value:
                    res.append(node)      
                node = node._right 
        return res

    def delete(self, value):
        del_list = self.search(value)
        for node in del_list:
            self._del(node)

    def _del(self, node: TreeNode):
        """
        1. 没有子节点：直接删除父节点指针
        2. 有一个子节点： 将父节点指向节点的指针指向节点的子节点
        3. 有两个子节点：找到右子树的最小节点M，将值赋值给节点，然后删除M
        """
        if node._left and node._right:
            min_node = node._right
            while min_node._left:
                min_node = min_node._left
            node._value = min_node._value
            node = min_node
        
        child = None
        if node._left: child = node._left
        elif node._right: child = node._right

        if not node._parent: self._root = child
        elif node._parent._left == node: node._parent._left = child
        else: node._parent._right = child

    def get_min(self):
        if not self._root:
            return None

        node = self._root
        while node._left:
            node = node._left
        return node._value

    def get_max(self):
        if not self._root:
            return None
        
        node = self._root
        while node._right:
            node = node._right
        return node._value

    def inorder(self):
        if not self._root:
            return []

        return self._inorder(self._root)

    def _inorder(self, node):
        if not node:
            return []

        res = []
        res.extend(self._inorder(node._left))
        res.append(node._value)
        res.extend(self._inorder(node._right))

        return res

    def __repr__(self):
        return self._draw_tree()

    def _bfs(self):
        if not self._root:
            return []

        res = []
        q = Queue()
        q.put((self._root, 1))

        while not q.empty():
            node, number = q.get()
            if node:
                res.append((node._value, number))
                q.put((node._left, number*2))
                q.put((node._right, number*2+1))
        
        return res

    def _draw_tree(self):
        nodes = self._bfs()

        if not nodes:
            return

        layer_num = int(math.log(nodes[-1][1], 2)) + 1

        prt_nums = []

        for i in range(layer_num):
            prt_nums.append([None]*2**i)

        for v, p in nodes:
            row = int(math.log(p, 2))
            col = p % 2**row
            prt_nums[row][col] = v

        prt_str = ''
        for l in prt_nums:
            prt_str += str(l)[1:-1] + '\n'

        return prt_str

if __name__ == '__main__':
    nums = [4, 2, 5, 6, 1, 7, 3]
    bst = BinarySearchTree(nums)
    print(bst)

    bst.insert(1)
    bst.insert(4)
    print(bst)

    for node in bst.search(2):
        print(node._parent._value, node._value)

    bst.insert(6)
    bst.insert(7)
    print(bst)
    bst.delete(7)
    print(bst)
    bst.delete(6)
    print(bst)
    bst.delete(4)
    print(bst)

    print(bst.get_max())
    print(bst.get_min())