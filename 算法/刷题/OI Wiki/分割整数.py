# 分割整数
# https://oi-wiki.org/search/dfs/ 第一个例题

# 把正整数n分解为m个不同的正整数，如6 = 1 + 2 3，排在后面的数必须大于等于前面的数，输出所有方案。

from typing import List, Optional


def divide(n: int, k: int, minimum: int) -> Optional[List[List[int]]]:
    result = []
    if n == 0:
        return [[]]
    if k == 1 and n >= minimum:
        return [[n]]
    for i in range(minimum, n + 1):
        result.extend([[i] + x for x in divide(n - i, k - 1, i)])
    return result


print(divide(6, 3, 1))
