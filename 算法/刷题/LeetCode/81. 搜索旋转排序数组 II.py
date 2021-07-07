# Tags: 旋转数组

# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,5,6,0,0,1,2], target = 0
# 输出：true
# 示例 2：
#
# 输入：nums = [2,5,6,0,0,1,2], target = 3
# 输出：false
#
#
# 提示：
#
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -104 <= target <= 104
#
#
# 进阶：
#
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 相比于原来没有重复的版本，这个版本可能会出现nums[l] == nums[r] == n，无法判断往那边取舍。所以最差是O(n)。
# 不过因为数组很小，其实直接一个一个比较也不慢。

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (l + r) // 2
            n = nums[i]
            if n == target:
                return True
            if nums[l] == nums[r] == n:
                # 特殊之处在这里
                l, r = l + 1, r - 1
            elif nums[l] <= n:
                if nums[l] <= target < n:
                    r = i - 1
                else:
                    l = i + 1
            else:
                if n < target <= nums[r]:
                    l = i + 1
                else:
                    r = i - 1
        return False

    def search1(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[r] < target < nums[l]:
                return False
            if nums[l] < nums[r]:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[l] == nums[r] == nums[mid]:
                l, r = l + 1, r - 1
            elif nums[l] <= target:
                # 后面这部分就是两种思路啦，当然可以寻求化简，把取左和取右汇总
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
                return False
        return False


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution().search([1], 0))
print(Solution().search([3, 1], 0))

print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0))
print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0))
print(Solution().search([3, 1, 2, 3, 3, 3, 3], 2))
print(Solution().search([1, 0, 1, 1, 1], 0))
print(Solution().search([1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13))
print(Solution().search([2, 3, 5, 7, 1], 6))

print('---')

print(Solution().search1([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search1([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution().search1([1], 0))
print(Solution().search1([3, 1], 0))

print(Solution().search1([2, 5, 6, 0, 0, 1, 2], 0))
print(Solution().search1([2, 5, 6, 0, 0, 1, 2], 0))
print(Solution().search1([3, 1, 2, 3, 3, 3, 3], 2))
print(Solution().search1([1, 0, 1, 1, 1], 0))
print(Solution().search1([1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13))
print(Solution().search1([2, 3, 5, 7, 1], 6))
