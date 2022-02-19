# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/volume-of-histogram-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 官方题解给了三种方法。

# 第一种基于：一个位置上水的高度 = min(左边最高柱子高度, 右边最高柱子高度)，因而从左往右和从右往左各扫一遍，得到各个位置其左右最高柱子高度。
# 官方称此为DP，确实算吧，比较勉强。
# 时间：O(n)，空间：O(n)

# 第二种方法比较巧妙，和我的做法有点类似，就是扫一遍，能加水的话就加水。我记录左边高度，而该方法记录左边和所有中间的index。
# 如此，每次和栈顶比较高度，即可得到水量。
# 官方称此为单调栈。
# 时间：O(n)，空间：O(n)

# 第三种更巧妙。注意到和我的做法一样，本质上就是最高的那个点决定了左边和右边的水。这个方法用双指针，比如说目前左右最高是1和2，则中间至少
# 能有1的水高，两个指针向中移动，直到相遇在一个最高点，即可得到水量。
# 官方的双指针图示很棒。这里的启发是可以用双指针甚至更多指针找最大值！
# 时间：O(n)，空间：O(1)

# 我的方法，时间：O(n)，空间：O(1)
# 第一次从左往右，遇到更高的柱子就加水，并记录最高柱子位置，第二次从右往左，遇到更高的柱子加水。和双指针一样，本质上最高的点决定了左右的水量。
# 不过时间上回头扫了一些，最坏情况（最高点是第一个柱子）下O(2n)，最好是O(n)。

# 还有按行解的，稍微麻烦点，思路就是从高度1开始加水，左右两侧高度<=1的柱子就可以删掉了，再看高度2……
# 为了解决有10000高的柱子的情况，每次遍历可以记录接下来最低的柱子。
# 但这样要扫很多遍，时间复杂度还受柱子高度影响，不好。

# 别的方法的代码见“42. 接雨水.py”。

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        water = 0
        # 左到右
        current_water = 0
        current_height = 0
        current_height_index = 0
        for i, h in enumerate(height):
            if h >= current_height:
                water += current_water
                current_water = 0
                current_height = h
                current_height_index = i
            else:
                current_water += current_height - h
        # 右到左
        current_water = 0
        current_height = 0
        for i, h in enumerate(height[-1:current_height_index - len(height) - 1:-1]):
            if h >= current_height:
                water += current_water
                current_water = 0
                current_height = h
            else:
                current_water += current_height - h

        return water


print(Solution().trap([]))
print(Solution().trap([0]))
print(Solution().trap([1]))
print(Solution().trap([4, 2, 3]))
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([0, 1, 0, 2, 4, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 8, 1, 2, 1]))
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 5, 2, 2, 3, 4, 3, 7, 9]))
