# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 整数除法仅保留整数部分。
#
#
# 示例 1：
#
# 输入：s = "3+2*2"
# 输出：7
# 示例 2：
#
# 输入：s = " 3/2 "
# 输出：1
# 示例 3：
#
# 输入：s = " 3+5 / 2 "
# 输出：5
#
# 提示：
#
# 1 <= s.length <= 3 * 105
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
# 题目数据保证答案是一个 32-bit 整数
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/basic-calculator-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def calculate(self, s: str) -> int:
        # 先把加减分开
        # 再处理乘除
        s = ''.join([c for c in s if c != ' '])
        positive_parts = s.split('+')
        negative_parts = []
        for i, part in enumerate(positive_parts):
            parts = part.split('-')
            positive_parts[i] = parts[0]
            negative_parts.extend(parts[1:])

        # print(positive_parts, negative_parts)

        def calculate_multiplication_and_division(expression):
            is_number = False
            number = 0

            ans = 1
            multiply = True

            for c in '1*' + expression + '*1':
                if '0' <= c <= '9':
                    is_number = True
                    number = number * 10 + int(c)
                else:
                    if is_number:
                        if multiply:
                            ans *= number
                        else:
                            ans //= number
                        is_number = False
                        number = 0

                if c == '*':
                    multiply = True
                if c == '/':
                    multiply = False
            # print(expression, ans)
            return ans

        return sum(calculate_multiplication_and_division(x) for x in positive_parts) - \
               sum(calculate_multiplication_and_division(x) for x in negative_parts)


def test(S):
    for (s, ans) in S:
        solution = Solution()
        answer = solution.calculate(s)
        print('Answer for "' + s + '" is "' + str(answer) + '". Expecting "' + str(
            ans) + '". ' + 'CORRECT!' if ans == answer else 'WRONG!')


test([
    ('3+2*2', 7),
    (' 3/2 ', 1),
    (' 3+5 / 2 ', 5),
    ('2 + 3 - 6 / 3 + 8 * 5 - 2 + 9', 50)
])
