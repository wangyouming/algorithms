int binarySearch(int a[], int n, int value) {
    int low = 0;
    int high = n - 1;
    while (low <= high) {
        int mid = low + ((high - low) >> 1); //如果low比较大，(low + high)可能会溢出
        if (a[mid] == value) {
            return mid;
        } else if (a[mid] < value) {
            low = mid + 1; //如果写成low=mid，可能发生死循环，比如high=3,low=3时，如果a[3]不等于value，就会导致一直循环不退出
        } else {
            high = mid - 1;
        }
    }

    return -1;
}

int _binarySearch_recursive(int a[], int low, int high, int value) {
    if (low > high) return -1;
    int mid = low + ((high - low) >> 1);
    if (a[mid] == value) {
        return mid;
    } else if (a[mid] < value) {
        return _binarySearch_recursive(a, mid+1, high, value);
    } else {
        return _binarySearch_recursive(a, low, mid-1, value);
    }
}

int binarySearch_recursive(int a[], int n, int value) {
    return _binarySearch_recursive(a, 0, n-1, value);
}

int binarySearchFirstEqual(int a[], int n, int value) {
    int low = 0;
    int high = n - 1;
    while (low <= high) {
        int mid = low + ((high - low) >> 1);
        if (a[mid] > value) {
            high = mid - 1;
        } else if (a[mid] < value) {
            low = mid + 1;
        } else {
            if ((mid == 0) || a[mid - 1] != value) return mid;
            else high = mid - 1;
        }
    }
    return -1;
}

int binarySearchFirstEqual_(int a[], int n, int value) {//更简洁，但是不太好理解
    int low = 0;
    int high = n - 1;
    while (low <= high) {
        int mid = low + ((high - low) >> 1);
        if (a[mid] >= value) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    if (a[low] == value) return low;
    return -1;
}

int binarySearchLastEqual(int a[], int n, int value) {
    int low = 0;
    int high = n - 1;
    while (low <= high) {
        int mid = low + ((high - low) >> 1);
        if (a[mid] > value) {
            high = mid - 1;
        } else if (a[mid] < value) {
            low = mid + 1;
        } else {
            if ((mid == n - 1 ) || a[mid - 1] != value) return mid;
            else low = mid + 1;
        }
    }
    return -1;
}

int binarySearchFirstGreaterOrEqual(int a[], int n, int value) {
    int low = 0;
    int high = n - 1;
    while (low <= high) {
        int mid = low + ((high - low) >> 1);
        if (a[mid] >= value) {
            if ((mid == 0) || a[mid - 1] < value) return mid;
            else high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return -1;
}

int binarySearchLastLessOrEqual(int a[], int n, int value) {
    int low = 0;
    int high = n - 1;
    while (low <= high) {
        int mid = low + ((high - low) >> 1);
        if (a[mid] > value) {
            high = mid - 1;
        } else {
            if ((mid == n - 1) || (a[mid] + 1 > value)) return mid;
            else low = mid + 1;
        }
    }
    return -1;
}