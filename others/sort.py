from typing import List

def bubbleSort(nums: List[int]):
    n = len(nums)
    if n <= 1: return
    
    for i in range(n):
        flag = False
        for j in range(n - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            flag = True
        if not flag: break

def insertionSort(nums: List[int]):
    n = len(nums)
    if n <= 1: return
    
    for i in range(n):
        value = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] > value:
                nums[j+1] = nums[j]
            else:
                break
            j -= 1
        nums[j+1] = value 

def selectionSort(nums: List[int]):
    n = len(nums)
    for i in range(n - 1):
        idx = i
        for j in range(i+1, n):
            if nums[j] < nums[idx]:
                idx = i
        if i != idx:
            nums[i], nums[idx] = nums[idx], nums[i]
        
def mergeSort(nums: List[int]):
    def _merge(nums: List[int], p: int, q: int, r: int):
        tmp = [None]*(r-p+1)
        i, j, k = p, q+1, 0
        while i <= q and j <= r:
            if nums[i] <= nums[j]:
                tmp[k] = nums[i]
                k += 1
                i += 1
            else:
                tmp[k] = nums[j]
                k += 1
                j +=1
        
        start = i, end = q
        if j <= r: start = j, end = r
        tmp[k, end-start+1] = nums[start: end-start+1]
        nums[:] = tmp[:]
        
    def _mergeSort(nums: List[int], p: int, r: int):
        if p >= r: return
        q = p + (r - p) >> 2
        _mergeSort(nums, p, q)
        _mergeSort(nums, q+1, r)
        _merge(nums, p, q, r)
    
    _mergeSort(nums, 0, len(nums) - 1)

def quickSort(nums: List[int]):
    def _partition(nums: List[int], p: int, r: int) -> int:
        pivot = nums[r]
        i = p
        for j in range(p, r):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]

        return i
    def _quickSort(nums: List[int], p: int, r: int):
        if p >= r: return
        q = _partition(nums, p, r)
        _quickSort(nums, p, q-1)
        _quickSort(nums, q+1, r)

    _quickSort(nums, 0, len(nums)-1)

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