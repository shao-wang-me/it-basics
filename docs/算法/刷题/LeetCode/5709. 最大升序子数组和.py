from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        current_sum = 0
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
            ans = max(ans, current_sum)
        return ans


def test(cases):
    for nums in cases:
        solution = Solution()
        print(solution.maxAscendingSum(nums))


test([
    [10, 20, 30, 5, 10, 50],
    [10, 20, 30, 40, 50],
    [12, 17, 15, 13, 10, 11, 12],
    [100, 10, 1]
])
