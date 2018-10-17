
void selectionSort(int a[], int n) {
    int tmp;
    for (int i = 0; i < n - 1; ++i) {
        int index = i;
        for (int j = i+1; j < n; ++j) {
            if (a[j] < a[index]) 
            index = j;
        }
        if (index != i) {
            tmp = a[i];
            a[i] = a[index];
            a[index] = tmp;
        }
    }
}

/*
选择排序的最好情况时间复杂度、最坏情况时间复杂度、平均时间复杂度都为O(n^2).
选择排序每次都要找剩余未排序元素中的最小值，并和前面的元素交换位置，这样破坏了稳定性，是不稳定的排序算法
*/