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
