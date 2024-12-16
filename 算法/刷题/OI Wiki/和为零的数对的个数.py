# 和为零的数对的个数
# https://oi-wiki.org/basic/enumerate/

# 一个数组中的数互不相同，求其中和为0的数对的个数

# 虽然这是在介绍枚举，但这题的做法显然是用一个set比较合适

from typing import List


def sum_zero(nums: List[int]) -> int:
    result = 0
    numbers = set()
    for n in nums:
        if -n in numbers:
            result += 1
        else:
            numbers.add(n)
    return result


print(sum_zero([0, 1, -1, 2, 5]))
print(sum_zero([0, 1, -1, 2, -2]))
print(sum_zero([0, 1, -1, 2, 5, 9, -5]))
