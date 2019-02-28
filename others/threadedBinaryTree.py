class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.is_left_thread = False
        self.is_right_thread = False

def inThreading(root: ListNode):
    pre = None
    def threading(node: ListNode):    
        nonlocal pre
        if not node: return

        threading(node.left)

        if not node.left:
            node.is_left_thread = True
            node.left = pre

        if pre and not pre.right:
            pre.is_right_thread = True
            pre.right = node
        
        pre = node

        threading(node.right)
    
    threading(root)

def preThreading(root: ListNode):
    pre = None
    def threading(node: ListNode):
        nonlocal pre
        if not node: return
        
        if not node.left:
            node.is_left_thread = True
            node.left = pre
        if pre and not pre.right:
            pre.is_right_thread = True
            pre.right= node
        
        pre = node

        if not node.is_left_thread:
            threading(node.left)
        if not node.is_right_thread:
            threading(node.right)
    threading(root)

def inorderTraverse(node: ListNode):
    cur = node
    while cur:
        while not cur.is_left_thread:
            cur = cur.left
        print(cur.val)
        while cur.is_right_thread:
            cur = cur.right
            print(cur.val)
        cur = cur.right

def preorderTraverse(node: ListNode):
    cur = node
    while cur:
        print(cur.val)
        if not cur.is_left_thread:
            cur = cur.left
        else:
            cur = cur.right

if __name__ == '__main__':
    def createTree() -> ListNode:
        nodes = []# A...J
        for i in range(10):
            char = chr(ord('A') + i)
            nodes.append(ListNode(char))

        for i in range(len(nodes)//2):
            left_idx = (i + 1) * 2 - 1
            right_idx = (i + 1) * 2
            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]
        return nodes[0]

    node = createTree()
    inThreading(node)
    inorderTraverse(node)

    print('-'* 10)

    node = createTree()
    preThreading(node)
    preorderTraverse(node)