# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
# 若旋转 4 次，则可以得到 [0,1,2,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
#
# 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
#
#
#
# 示例 1：
#
# 输入：nums = [3,4,5,1,2]
# 输出：1
# 解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
# 示例 2：
#
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
# 解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
# 示例 3：
#
# 输入：nums = [11,13,15,17]
# 输出：11
# 解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums 中的所有整数 互不相同
# nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 还是旋转数组+搜索。
# 这种题目要仔细列举各种可能的情况，判断要留哪部分，终止条件是什么。
# 每个人的解法，判断逻辑写法可能会有区别，不要紧，重点是分清情况。

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid] < nums[r]:
                r = mid - 1
            elif nums[r] < nums[l] <= nums[mid]:
                l = mid + 1
            elif nums[mid] < nums[r] < nums[l]:
                r = mid
            else:
                raise Exception
        return nums[l]


print(Solution().findMin([3, 4, 5, 1, 2]))
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
print(Solution().findMin([11, 13, 15, 17]))
print(Solution().findMin([5, 1, 2, 3, 4]))
