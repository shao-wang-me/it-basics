#include <cstdio>
#include <iostream>


int m, arr[103];  // arr 用于记录方案
void dfs(int n, int i, int a) {
    if (n == 0) {
        for (int j = 1; j <= i - 1; ++j) printf("%d ", arr[j]);
        printf("\n");
    }
    if (i <= m) {
        for (int j = a; j <= n; ++j) {
          arr[i] = j;
          dfs(n - j, i + 1, j);  // 请仔细思考该行含义。
        }
    }
}

int main() {
    // 主函数
    m = 3;
    dfs(6, 1, 1);
    return 0;
}
