# Tags: 括号、栈

# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
# 示例 1：
#
# 输入：s = "()"
# 输出：true
#
# 示例2：
#
# 输入：s = "()[]{}"
# 输出：true
#
# 示例3：
#
# 输入：s = "(]"
# 输出：false
#
# 示例4：
#
# 输入：s = "([)]"
# 输出：false
#
# 示例5：
#
# 输入：s = "{[]}"
# 输出：true
#
# 提示：
#
# 1 <= s.length <= 104
# s 仅由括号 '()[]{}' 组成
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for c in s:
            if c in brackets.keys():
                stack.append(c)
            elif c in brackets.values():
                if not stack or brackets[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
        return not stack


print(Solution().isValid('()'))
print(Solution().isValid('()[]{}'))
print(Solution().isValid('(]'))
print(Solution().isValid('([)]'))
print(Solution().isValid('{[]}'))
