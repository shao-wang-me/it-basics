# Tags: 回溯、DFS、DP

# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
#
#
# 提示：
#
# 1 <= n <= 8
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from functools import lru_cache
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 主要思路是在尾部添加括号，一个递归内是两个分支（可以有多个分支），递归内添加括号，当符合条件时，把结果加入进去。
        # 回溯（DFS），官方解法二
        # 这是一种常见的解法，递归栈隐式地构建了问题搜索树，并且是深度优先的。
        # 时间：据官方题解，是挺复杂的一个数字，不小，因为涉及到组合
        # 空间：ans的大小应该和时间复杂度一样，递归栈的空间是O(n)，因为最多有2n个递归调用
        ans = []

        def dfs(S: str, left: int, right: int):
            if len(S) == n * 2:
                ans.append(S)
                return
            if left < n:
                dfs(S + '(', left + 1, right)
            if right < left:
                dfs(S + ')', left, right + 1)

        dfs('', 0, 0)
        return ans

    @lru_cache(None)
    def generateParenthesis_decrease_and_conquer(self, n: int) -> List[str]:
        # 类似官方解法三
        # 算是用递归的减治法吧，由于有重复空间，也是DP
        # 思路是可以把每个组合看成是形如(a)b的样子，其中a和b都是合法组合，且都可以为空
        # 由于子问题的可能是重复的，我们可以对结果进行“缓存/记忆”。官方题解是用的functools.@lru_cache(None)。
        if n == 0:
            return ['']
        ans = []
        for i in range(n):
            ans.extend(
                ['(' + x + ')' + y for x in self.generateParenthesis(i) for y in self.generateParenthesis(n - 1 - i)])
        return ans


print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(4))
print(Solution().generateParenthesis(5))
print(Solution().generateParenthesis(6))
print(Solution().generateParenthesis(7))
print(Solution().generateParenthesis(8))

print(Solution().generateParenthesis_decrease_and_conquer(1))
print(Solution().generateParenthesis_decrease_and_conquer(2))
print(Solution().generateParenthesis_decrease_and_conquer(3))
print(Solution().generateParenthesis_decrease_and_conquer(4))
print(Solution().generateParenthesis_decrease_and_conquer(5))
print(Solution().generateParenthesis_decrease_and_conquer(6))
print(Solution().generateParenthesis_decrease_and_conquer(7))
print(Solution().generateParenthesis_decrease_and_conquer(8))
