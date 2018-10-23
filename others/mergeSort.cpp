#include <vector>

void _merge(int a[], int p, int q, int r) {
    int i = p, j = q+1, k = 0; 
    std::vector<int> tmp(r-p+1);
    while (i <= q && j <= r) {
        if (a[i] <= a[j]) {
            tmp[k++] = a[i++];
        } else {
            tmp[k++] = a[j++];
        }
        int start = i, end = q;
        if (j <= r) start = j, end = r;

        while (start <= end) {
            tmp[k++] = a[start++];
        }

        for (int i = 0; i <= r-p; ++i) {
            a[p++] = tmp[i];
        }
    }
}

void _mergeSort(int a[], int p, int r) {
    if (p >= r) return;

    int q = (p + r) / 2;
    _mergeSort(a, p, q);
    _mergeSort(a, q+1, r);    
    _merge(a, p, q, r);
}

void mergeSort(int a[], int n) {
    _mergeSort(a, 0, n-1);
}
/*
T(a) = T(b) + T(c) + K，其中K等于将两个子问题b、c合并成问题a的结果所消耗的时间
T(1) = C; n = 1时，只需要常量级的执行时间
T(n) = 2*T(n/2) + n
     = 2*(2*T(n/4) + n/2) + n
     = 2^kT(n/2^k) + kn
n/2^k = 1 => k = log2(n) => T(n) = C(n) + nlog2(n) => O(nlogn)
不管是最好情况、最坏情况、平均情况复杂度都是O(nlogn)

尽管每次合并操作都需要申请额外的内存空间，但在合并完成之后，临时开辟的内存空间就被释放掉了。任意时刻，CPU只有一个函数在执行，也就只有一个临时的内存空间在使用。临时内存空间最大也不会超过n个数据的大小，所有空间复杂度是O(n)
*/