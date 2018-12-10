
public class BM {
    private static final int SIZE = 256;
    private void generateBC(char[] b, int m, int[] bc) {
        for (int i = 0; i < SIZE; ++i) {
            bc[i]= -1;
        }
        for (int i = 0; i < m; ++i) {
            int ascii = (int)b[i];
            bc[ascii] = i;
        }
    }

    private void generateGS(char[] b, int m, int[] suffix, boolean[] prefix) {
        for (int i = 0; i < m; ++i) {
            suffix[i] = -1;
            prefix[i] = false;
        }
        for (int i = 0; i < m - 1; ++i) {
            int j = i;
            int k = 0;
            while (j >=0 && b[j] == b[m-1-k]) {
                --j;
                ++k;
                suffix[k] = j+1;
            }
            if (j == -1) prefix[k] = true;
        }
    }

    private int moveByGS(int j, int m, int[] suffix, boolean[] prefix) {
        int k = m - 1 - j;
        if (suffix[k] != -1) return j - suffix[k] + 1;
        for (int r = j+2; r <= m-1; ++r) {
            if (prefix[m-r] == true) {
                return r;
            }
        }
        return m;
    }

    public int bm(char[] a, int n, char[] b, int m) {
        int[] bc = new int[SIZE];
        generateBC(b, m, bc);
        int[] suffix = new int[m];
        boolean[] prefix = new boolean[m];
        generateGS(b, m, suffix, prefix);
        int i = 0;
        while (i <= n-m) {
            int j;
            for (j = m -1; j >=0; --j) {
                if (a[i+j] != b[j]) break;
            }
            if (j < 0) {
                return i;
            }
            int x = j - bc[(int)a[j+i]];
            int y = 0;
            if (j < m-1) {
                y = moveByGS(j, m, suffix, prefix);
            }
            i = i + Math.max(x, y);
        }
        return -1;
    }
}