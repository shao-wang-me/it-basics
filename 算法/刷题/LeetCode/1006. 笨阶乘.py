# 通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。
#
# 相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。
#
# 例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。
#
# 另外，我们使用的除法是地板除法（floor division），所以10 * 9 / 8等于11。这保证结果是一个整数。
#
# 实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。
#
#
#
# 示例 1：
#
# 输入：4
# 输出：7
# 解释：7 = 4 * 3 / 2 + 1
# 示例 2：
#
# 输入：10
# 输出：12
# 解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
#
#
# 提示：
#
# 1 <= N <= 10000
# -2^31 <= answer <= 2^31 - 1 （答案保证符合 32 位整数。）
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/clumsy-factorial
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 用Python的eval()的话就作弊了，否则的话就直接按照循环算出来，O(n)。也可以化简为公式直接算，应该是最快的，O(1)。

# 数学化简（官解思路）：
# f(N) = N * (N - 1) // (N - 2) + (N - 3) - (N - 4) * (N - 5) // (N - 6) + (N - 7) - ...
# 其中，N * (N - 1) // (N - 2) = (N * (N - 2) + N) // (N - 2) = N + N // (N - 2)
# 其中，当N >= 5时，N // (N - 2) = 1
# 所以，当N >= 5时，N * (N - 1) // (N - 2) = (N * (N - 2) + N) // (N - 2) = N + 1
# 所以，当N >= 5时，f(N) = (N + 1) + (N + 3) - (N - 3) + (N - 7) - ...
# 举几个N >= 5情况，发现，当N >= 5时，f(N) = (N + 1) + (N + 3) - (N - 3) + (N - 7) - ... = N + 1 + 剩下不能消掉的部分
# 剩下不能消掉的部分，在N % 4分别为0、1、2、3时，分别为0、1、1、-2
# 所以，当N >= 5时
# f(N) = N + 1 (N % 4 = 0)
#        N + 2 (N % 4 = 1)
#        N + 2 (N % 4 = 2)
#        N - 2 (N % 4 = 3)
# 所以只要单独列N为1、2、3、4时的情况即可。

# 数学化简，我的方法见 笨阶乘.png


class Solution:
    def clumsy_作弊(self, N: int) -> int:
        # 作弊
        expression = ''
        ops = ['*', '//', '+', '-']
        for i in range(N):
            n = N - i
            expression += str(n) + ops[i % 4]
        expression = expression[:-2] if expression[-1] == '/' else expression[:-1]
        print('expression', expression)
        return eval(expression)

    def clumsy(self, N: int) -> int:
        number_of_groups = N // 4
        result = 0
        for i in range(number_of_groups):
            n = N - 4 * i
            x = n * (n - 1) // (n - 2)
            result += x if n == N else -x
            result += n - 3
        if N % 4 == 1:
            result += -1 if N > 3 else 1
        elif N % 4 == 2:
            result += -2 if N > 3 else 2
        elif N % 4 == 3:
            result += -6 if N > 3 else 6
        return result

    def clumsy_math(self, N: int) -> int:
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 6
        if N == 4:
            return 7
        remainder = N % 4
        if remainder == 0:
            return N + 1
        if remainder in [1, 2]:
            return N + 2
        if remainder == 3:
            return N - 1

    def clumsy_stack(self, N: int) -> int:
        # TODO 栈的方法
        pass


for i in range(1, 10):
    print(Solution().clumsy_作弊(i), Solution().clumsy(i), Solution().clumsy_math(i))
