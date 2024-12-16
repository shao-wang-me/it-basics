# Tags: 旋转数组、二分搜索

# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
#
#
# 示例 1：
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 示例 2：
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
# 提示：
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
#
#
# 进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 有点绕，但还是二分搜索，时间复杂度O(logn)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = nums[0], nums[len(nums) - 1]
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (l + r) // 2
            n = nums[i]
            if n == target:
                return i
            if left <= target:
                if left <= n < target:
                    l = i + 1
                else:
                    r = i - 1
            elif target <= right:
                if target < n <= right:
                    r = i - 1
                else:
                    l = i + 1
            else:
                return -1
        return -1

    def search1(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[r]:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[l] <= target:
                if nums[l] <= nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            elif target <= nums[r]:
                if target < nums[mid] <= nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                return -1
        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution().search([1], 0))
print(Solution().search([3, 1], 0))
print(Solution().search([2, 3, 5, 7, 1], 6))

print(Solution().search1([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search1([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution().search1([1], 0))
print(Solution().search1([3, 1], 0))
print(Solution().search1([2, 3, 5, 7, 1], 6))
