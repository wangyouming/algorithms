
int binarySearch(int nums[], int size, int value) {
    int lo = 0;
    int hi = size - 1;
    while (lo <= hi) {
        int mid = lo + ((hi - lo) >> 1);
        if (nums[mid] == value) {
            return mid;
        } else if (nums[mid] < value) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }

    return -1;
}

int _binarySearchRecursively(int nums[], int lo, int hi, int value) {
    if (lo > hi) return -1;
    int mid = lo + ((hi - lo) >> 1);
    if (nums[mid] == value) {
        return mid;
    } else if (nums[mid] < value) {
        return _binarySearchRecursively(nums, mid+1, hi, value);
    } else {
        return _binarySearchRecursively(nums, lo, mid-1, value);
    }
}

int binarySearchRecursively(int nums[], int size, int value) {
    return _binarySearchRecursively(nums, 0, size-1, value);
}

int binarySearchFirstEqual(int nums[], int size, int value) {
    int lo = 0;
    int hi = size - 1;
    while (lo <= hi) {
        int mid = lo + ((hi - lo) >> 1);
        if (nums[mid] > value) {
            hi = mid - 1;
        } else if (nums[mid] < value) {
            lo = mid + 1;
        } else {
            if ((mid == 0) || nums[mid - 1] != value) return mid;
            else hi = mid - 1;
        }
    }
    return -1;
}

int binarySearchLastEqual(int nums[], int size, int value) {
    int lo = 0;
    int hi = size - 1;
    while (lo <= hi) {
        int mid = lo + ((hi - lo) >> 1);
        if (nums[mid] > value) {
            hi = mid - 1;
        } else if (nums[mid] < value) {
            lo = mid + 1;
        } else {
            if ((mid == size - 1 ) || nums[mid - 1] != value) return mid;
            else lo = mid + 1;
        }
    }
    return -1;
}

int binarySearchFirstGreaterOrEqual(int nums[], int size, int value) {
    int lo = 0;
    int hi = size - 1;
    while (lo <= hi) {
        int mid = lo + ((hi - lo) >> 1);
        if (nums[mid] >= value) {
            if ((mid == 0) || nums[mid - 1] < value) return mid;
            else hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return -1;
}

int binarySearchLastLessOrEqual(int nums[], int size, int value) {
    int lo = 0;
    int hi = size - 1;
    while (lo <= hi) {
        int mid = lo + ((hi - lo) >> 1);
        if (nums[mid] > value) {
            hi = mid - 1;
        } else {
            if ((mid == size - 1) || (nums[mid] + 1 > value)) return mid;
            else lo = mid + 1;
        }
    }
    return -1;
}
