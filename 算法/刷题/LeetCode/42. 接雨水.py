# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# 示例 1：
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# 示例 2：
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
# 提示：
#
# n == height.length
# 0 <= n <= 3 * 104
# 0 <= height[i] <= 105
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/trapping-rain-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 这个和“面试题 17.12. 直方图的水量”是一样的。
# 这里把双指针的方法做一下。

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针
        water = 0
        l, r = 0, len(height) - 1
        left_max_index, right_max_index = l, r
        while l <= r:
            if height[l] < height[left_max_index]:
                water += height[left_max_index] - height[l]
            else:
                left_max_index = l
            if height[r] < height[right_max_index]:
                water += height[right_max_index] - height[r]
            else:
                right_max_index = r
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return water

    def trap_stack(self, height: List[int]) -> int:
        # TODO 栈的方法
        pass


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))
