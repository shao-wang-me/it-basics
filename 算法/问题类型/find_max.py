# 找到数组最大值

from typing import List


def maximum1(nums: List[int]) -> int:
    result = nums[0]
    for n in nums:
        if n > result:
            result = n
    return result


def maximum2(nums: List[int]) -> int:
    """双指针找数组最大值。正常肯定不会这样做，但有的题可以在这个过程做事情。甚至是多指针，任意方向。"""
    result = nums[0]
    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l] > nums[r]:
            result = max(result, nums[l])
            r -= 1
        else:
            result = max(result, nums[r])
            l += 1
    return result


print(maximum1([4, 1, 2, 5, 7, 3, 5, 4]))
print(maximum2([4, 1, 2, 5, 7, 3, 5, 4]))
print(maximum1([1, 2, 3, 4, 5, 6, 7, 8]))
print(maximum2([1, 2, 3, 4, 5, 6, 7, 8]))
