from typing import List, Type

class Heap:
    @staticmethod
    def heapify(vals: List[Type]):
        if len(vals) <= 1: return
        for i in range((len(vals)-2)//2, -1, -1):
            Heap.heapdown(vals, i)

    @staticmethod
    def heappush(vals: List[Type], val: Type):
        vals.append(val)
        Heap.heapup(vals, len(vals)-1)

    @staticmethod
    def heappop(vals: List[Type]) -> Type:
        val = Heap.heaptop(vals)
        last = vals.pop()
        if len(vals):
            vals[0] = last
            Heap.heapdown(vals, 0)
        return val

    @staticmethod
    def heaptop(vals: List[Type]) -> Type:
        return vals[0]

    @staticmethod
    def heapdown(vals: List[Type], idx: int) -> None:
        Heap._heapdown_with_end(vals, idx, len(vals))
    
    @staticmethod
    def _heapdown_with_end(vals: List[Type], idx: int, end: int) -> None:
        while True:
            min_idx = idx
            left_child = 2*idx + 1
            right_child = 2*idx + 2
            if left_child < end and vals[left_child] < vals[idx]: min_idx = left_child
            if right_child < end and vals[right_child] < vals[min_idx]: min_idx = right_child
            if min_idx == idx: break
            vals[idx], vals[min_idx] = vals[min_idx], vals[idx]
            idx = min_idx

    @staticmethod
    def heapup(vals: List[Type], idx: int) -> None:
        parent_idx = (idx - 1) // 2
        while parent_idx >= 0 and vals[idx] < vals[parent_idx]:
            vals[parent_idx], vals[idx] = vals[idx], vals[parent_idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2
    
    @staticmethod
    def prettify(vals: List[Type]) -> str:
        import math
        ret = ''
        for idx, val in enumerate(vals):
            ret += str(val)
            if idx == 2 ** int(math.log(idx + 1, 2) + 1) - 2 or idx == len(vals) - 1:
                ret += '\n'
            else:
                ret += ', '
        return ret
    
    @staticmethod
    def heapsort(vals: List[Type], ascending=False) -> None:
        n = len(vals)
        if n <= 1: return
        Heap.heapify(vals)
        while n > 1:
            vals[0], vals[n-1] = vals[n-1], vals[0]
            n -= 1
            Heap._heapdown_with_end(vals, 0, n)
        if ascending: vals.reverse()

class PriorityQueue:
    def __init__(self):
        self.vals = []
    
    def __len__(self):
        return len(self.vals)
    
    def __bool__(self):
        return len(self.vals) > 0
    
    def put(self, val):
        Heap.heappush(self.vals, val)
    
    def get(self):
        return Heap.heappop(self.vals)
    
    def heapup(self, val):
        idx = self.vals.index(val)
        Heap.heapup(self.vals, idx)

if __name__ == '__main__':
    nums = list(range(10))
    import random
    random.shuffle(nums) 

    print("random nums: ", nums, "\n")

    heap_nums = []

    while nums:
        Heap.heappush(heap_nums, nums.pop())

    print("heapify nums:")
    print(Heap.prettify(heap_nums))

    print("heappop all nums: ")    
    while heap_nums:
        print(Heap.heappop(heap_nums), end=" ")
    print("\n")

    nums = list(range(10))
    random.shuffle(nums)
    Heap.heapsort(nums, ascending=True)
    print("heapsorted nums: ")
    print(nums, "\n")

    random.shuffle(nums)
    pq = PriorityQueue()
    while nums:
        pq.put(nums.pop())
    print("PriorityQueue nums: ")
    while pq:
        print(pq.get(), end=" ")