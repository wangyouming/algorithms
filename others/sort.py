from typing import List

def bubbleSort(nums: List[int]):
    n = len(nums)
    for i in range(n-1):
        flag = True
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1], nums[j+1], nums[j]
                flag = False
        if flag: break
    
def insertionSort(nums: List[int]):
    n = len(nums)
    for i in range(1, n):
        value = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] > value:
                nums[j+1] = nums[j]
                j -= 1
            else:
                break
        nums[j+1] = value 

def selectionSort(nums: List[int]):
    n = len(nums)
    for i in range(n-1):
        idx = i
        for j in range(i+1, n):
            if nums[j] < nums[idx]:
                idx = j
        if i != idx:
            nums[i], nums[idx] = nums[idx], nums[i]
        
def mergeSort(nums: List[int]):
    def _merge(nums: List[int], p: int, q: int, r: int):
        tmp = [None]*(r-p)
        i, j, k = p, q, 0
        while i < q and j < r:
            if nums[i] <= nums[j]:
                tmp[k] = nums[i]
                k += 1
                i += 1
            else:
                tmp[k] = nums[j]
                k += 1
                j +=1
        
        start, end = i, q 
        if j < r: start, end = j, r
        tmp[k:] = nums[start:end]
        nums[p:r] = tmp[:]
        
    def _mergeSort(nums: List[int], p: int, r: int):
        if r - p <= 1: return
        q = p + ((r - p) >> 1)
        _mergeSort(nums, p, q)
        _mergeSort(nums, q, r)
        _merge(nums, p, q, r)
    
    _mergeSort(nums, 0, len(nums))

def quickSort(nums: List[int]):
    def _partition(nums: List[int], p: int, r: int) -> int:
        pivot = nums[r-1]
        i = p
        for j in range(p, r-1):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r-1] = nums[r-1], nums[i]
        return i

    def _quickSort(nums: List[int], p: int, r: int):
        if r - p <= 1: return
        q = _partition(nums, p, r)
        _quickSort(nums, p, q)
        _quickSort(nums, q, r)

    _quickSort(nums, 0, len(nums))

def countingSort(nums: List[int]):
    n = len(nums)
    if n <= 1: return
    max_num = max(nums)
    counts = [0] * (max_num + 1)
    for i in range(n):
        counts[nums[i]] += 1
    
    for i in range(1, max_num+1):
        counts[i] = counts[i-1]+counts[i]

    tmp = [None]*n
    for i in range(n):
        idx = counts[nums[i]] - 1
        tmp[idx] = nums[i]
        counts[nums[i]] -= 1

    nums[:] = tmp[:]

def kthElement(nums: List[int], k: int):
    def _partition(nums: List[int], p: int, r: int):
        pivot = nums[r-1]
        i = p
        for j in range(p, r-1):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r-1] = nums[r-1], nums[i]

        return i

    def _kthElement(nums: List[int], p: int, r: int, k: int):
        q = _partition(nums, p, r)
        if q == k: return nums[k]
        elif q < k: return _kthElement(nums, q, r, k)
        else: return _kthElement(nums, p, q, k)
        
    assert(k >= 0 and k < len(nums))
    return _kthElement(nums, 0, len(nums), k)

if __name__ == '__main__':
    import random
    nums = [2, 5, 1, 3]
    
    random.shuffle(nums)
    bubbleSort(nums)
    print(nums)

    random.shuffle(nums)
    insertionSort(nums)
    print(nums)

    random.shuffle(nums)
    selectionSort(nums)
    print(nums)

    random.shuffle(nums)
    mergeSort(nums)
    print(nums)

    random.shuffle(nums)
    quickSort(nums)
    print(nums)

    random.shuffle(nums)
    countingSort(nums)
    print(nums)

    random.shuffle(nums)
    val = kthElement(nums, 2)
    print(val)
