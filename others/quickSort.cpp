void swap(int a[], int i, int j) {
    int tmp = a[j];
    a[j] = a[i];
    a[i] = tmp;
}

int _partition(int a[], int p, int r) {
    int pivot = a[r];
    int i = p; //p..i-1小于pivot
    for (int j = p; j <= r-1; ++j) {
        if (a[j] < pivot) {
            swap(a, i, j);
            ++i;                        
        }
    }
    swap(a, i, r);
    return i;
}

void _quickSort(int a[], int p, int r) {
    if (p >= r) return;
    int q = _partition(a, p, r);
    _quickSort(a, p, q-1);
    _quickSort(a, q+1, r);
}

void quickSort(int a[], int n) {
    _quickSort(a, 0, n-1);
}
/*
因为分区的过程设计交换操作，如果数组中有两个8，其中一个是pivot，经过分区处理之后，后面的8就有可能被放到了另一个8的前面，先后顺序就颠倒了，所以快速排序并不是一个稳定的排序算法
归并排序的处理过程是由上而下的，先处理子问题，然后再合并；快排相反，处理过程是由上而下的，先分区，然后再处理子问题。
归并排序虽然是稳定的、时间复杂度为O(nlongn)的排序算法，但是它是非原地排序算法。快速排序通过设计巧妙的原地分区函数，可以实现原地排序。
T(n)在大部分情况下的时间复杂度都可以做到O(nlogn),之有在极端情况下，才会退化到O(n^2)。而且，我们也有很多方法将这个概率讲到很低。
*/