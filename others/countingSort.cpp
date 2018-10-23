#include <vector>

void countingSort(int a[], int n) {
    if (n <= 1) return;
    int max = a[0];
    for (int i = 1; i < n; ++i) {
        if (max < a[i]) {
            max = a[i];
        }
    }

    std::vector<int> c(max + 1);
    for (int i = 0; i <= max; ++i) {
        c[i] = 0;
    }

    for (int i = 0; i < n; ++i) {
        c[a[i]]++;
    }

    for (int i = 1; i <= max; ++i) {
        c[i] = c[i-1] + c[i];
    }

    std::vector<int> tmp(n);
    for (int i = n-1; i >= 0; --i) {
        int index = c[a[i]] - 1;
        tmp[index] = a[i];
        c[a[i]]--;
    }

    for (int i = 0; i < n; ++i) {
        a[i] = tmp[i];
    }
}