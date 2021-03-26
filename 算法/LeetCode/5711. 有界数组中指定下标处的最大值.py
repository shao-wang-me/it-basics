# 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
#
# nums.length == n
# nums[i] 是 正整数 ，其中 0 <= i < n
# abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
# nums 中所有元素之和不超过 maxSum
# nums[index] 的值被 最大化
# 返回你所构造的数组中的 nums[index] 。
#
# 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。
#
#
#
# 示例 1：
#
# 输入：n = 4, index = 2,  maxSum = 6
# 输出：2
# 解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
# 示例 2：
#
# 输入：n = 6, index = 1,  maxSum = 10
# 输出：3
#
#
# 提示：
#
# 1 <= n <= maxSum <= 109
# 0 <= index < n

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l, r = 1, maxSum - (n - 1)
        best_x = None
        best_summary = 0
        while l <= r:
            x = (l + r) // 2
            left_distance = min(x - 1, index)
            right_distance = min(x - 1, n - 1 - index)
            left_size = left_distance + 1
            right_size = right_distance + 1
            left_sum = (x * 2 - left_distance) * left_size / 2
            right_sum = (x * 2 - right_distance) * right_size / 2
            remain_size = n - left_size - right_size + 1
            summary = left_sum + right_sum - x + remain_size * 1
            if summary == maxSum:
                return x
            if summary < maxSum:
                if maxSum - summary < maxSum - best_summary:
                    best_x = x
                    best_summary = summary
                l = x + 1
            else:
                r = x - 1
        return best_x


def test(cases):
    for n, index, maxSum in cases:
        solution = Solution()
        print(solution.maxValue(n, index, maxSum))


test([
    (4, 2, 6),  # 2
    (6, 1, 10),  # 3
    (3, 2, 18)  # 7
])
