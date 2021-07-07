# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
#
#
# 示例 1：
#
# 输入：s = "1 + 1"
# 输出：2
# 示例 2：
#
# 输入：s = " 2-1 + 2 "
# 输出：3
# 示例 3：
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#
#
# 提示：
#
# 1 <= s.length <= 3 * 105
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/basic-calculator
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def calculate(self, s: str) -> int:
        # 应该数字都是正整数
        # 先考虑不带括号的，应该比较简单，就依序读取数字和运算符即可，空格直接忽略
        # 有括号的话，要考虑括号什么时候结束
        # 本质上来说是一个树？类似于AST？
        # 正规军的做法可能是所谓”逆波兰式“去化简，但在这里不管怎样都是用栈做！
        #
        # 因为只有加减，其实可以一遍考虑，只需要把减号和括号的组合放在一起考虑，把减号内的符号反过来即可
        # 当然啦，作弊就是直接return eval(s)，哈哈哈
        #
        # 引用官方题解：
        # > 与字符串中当前位置的运算符有关；
        # > 如果当前位置处于一系列括号之内，则也与这些括号前面的运算符有关：每当遇到一个以 -− 号开头的括号，则意味着此后的符号都要被「翻转」。
        # >
        # > 作者：LeetCode-Solution
        # > 链接：https://leetcode-cn.com/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode-solution-jvir/
        # > 来源：力扣（LeetCode）
        # > 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        ans = 0

        is_number = False
        number = 0

        positive = [True, True]

        for c in s + '+ 0':
            if c == ' ':
                continue

            if '0' <= c <= '9':
                is_number = True
                number = number * 10 + int(c)
            else:
                if is_number:
                    ans += number if positive[-1] else -number
                    number = 0
                is_number = False

            if c == '(':
                positive.append(positive[-1])

            if c == ')':
                positive.pop()

            if c == '+':
                positive[-1] = True if positive[-2] else False
            if c == '-':
                positive[-1] = False if positive[-2] else True

        return ans


def test(S):
    for (s, ans) in S:
        solution = Solution()
        answer = solution.calculate(s)
        print('Answer for "' + s + '" is: "' + str(answer) + '". Expecting: "' + str(
            ans) + ". " + ('CORRECT!' if answer == ans else 'WRONG!'))


test([
    ('1 + 1', 2),
    ('2-1 + 2', 3),
    ('(1+(4+5+2)-3)+(6+8)', 23),
    ('1 - (2 + (3 - 5) - (2- (7 - (8-9))))', -5)
])
