# 我们把玻璃杯摆成金字塔的形状，其中第一层有1个玻璃杯，第二层有2个，依次类推到第100层，每个玻璃杯(250ml)将盛有香槟。
#
# 从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。
# 当左右两边的杯子也满了，就会等流量的流向它们左右两边的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上）
#
# 例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。
# 在倒三杯香槟后，第二层的香槟满了 - 此时总共有三个满的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示。
#
# 现在当倾倒了非负整数杯香槟后，返回第 i 行 j 个玻璃杯所盛放的香槟占玻璃杯容积的比例（i 和 j都从0开始）。

# 示例 1:
# 输入: poured(倾倒香槟总杯数) = 1, query_glass(杯子的位置数) = 1, query_row(行数) = 1
# 输出: 0.0
# 解释: 我们在顶层（下标是（0，0））倒了一杯香槟后，没有溢出，因此所有在顶层以下的玻璃杯都是空的。
#
# 示例 2:
# 输入: poured(倾倒香槟总杯数) = 2, query_glass(杯子的位置数) = 1, query_row(行数) = 1
# 输出: 0.5
# 解释: 我们在顶层（下标是（0，0）倒了两杯香槟后，有一杯量的香槟将从顶层溢出，位于（1，0）的玻璃杯和（1，1）的玻璃杯平分了这一杯香槟，所以每个玻璃杯有一半的香槟。
# 注意:
#
# poured的范围[0, 10 ^ 9]。
# query_glass和query_row的范围[0, 99]。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/champagne-tower
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import Dict


class Solution:
    # 从需要计算的Glass向上算
    # 子问题的空间是重复的，所以动归
    # Python是可以简单地用tuple作为dict的key
    # Java的话可以用数组，并且是一维数组（手动算第i行第j个被子在数组中的index）

    CAPACITY = 1

    def __init__(self):
        self.poured = None
        self.mem = {}

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        self.poured = poured
        return self.inflow_result(query_row, query_glass)['remain']

    def inflow_result(self, i: int, j: int) -> Dict[str, any]:
        if (i, j) in self.mem:
            return self.mem[(i, j)]
        if i < 0:
            return {'remain': None, 'outflow': self.poured}
        if j < 0 or j > i:
            return {'remain': None, 'outflow': 0}
        inflow = self.inflow_result(i - 1, j - 1)['outflow'] / 2 + self.inflow_result(i - 1, j)['outflow'] / 2
        if inflow > self.CAPACITY:
            remain = self.CAPACITY
            outflow = inflow - self.CAPACITY
        else:
            remain = inflow
            outflow = 0
        self.mem[(i, j)] = {'remain': remain, 'outflow': outflow}
        return self.mem[(i, j)]


class Solution1:
    # 面对对象OOD办法，主要考虑设计
    def __init__(self):
        self.poured = None
        self.glasses = {}

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        self.poured = poured
        self.pour(query_row, query_glass)

        print('[Glasses]')
        for i in range(query_row + 1):
            row_string = ''
            for j in range(i):
                if (i, j) in self.glasses:
                    row_string += str(self.glasses[(i, j)].water) + ','
            print(i, row_string[:-1])
        print('[Glasses end]')

        return self.glasses[(query_row, query_glass)].water

    def pour(self, i: int, j: int) -> float:
        if (i, j) in self.glasses:
            return self.glasses[(i, j)].overflow
        if i < 0:
            return self.poured
        if j < 0 or j > i:
            return 0
        inflow = self.pour(i - 1, j - 1) / 2 + self.pour(i - 1, j) / 2
        glass = Glass()
        glass.fill(inflow)
        self.glasses[(i, j)] = glass
        return self.glasses[(i, j)].overflow


class Glass:
    CAPACITY = 0.25

    def __init__(self) -> None:
        self.water = 0
        self.inflow = 0
        self.overflow = 0

    def fill(self, volume: float) -> float:
        self.inflow += volume
        if self.water + volume > self.CAPACITY:
            overflow = volume + self.water - self.CAPACITY
            self.water = self.CAPACITY
            self.overflow += overflow
            return overflow
        else:
            self.water += volume
            return 0


class GlassInStack(Glass):
    def __init__(
            self,
            left_child: 'Glass' = None,
            right_child: 'Glass' = None,
            left_parent: 'Glass' = None,
            right_parent: 'Glass' = None
    ) -> None:
        super().__init__()
        self.left_child = left_child
        self.right_child = right_child
        self.left_parent = left_parent
        self.right_parent = right_parent

    def fill(self, volume: float) -> float:
        overflow = super().fill(volume)
        if overflow:
            if self.left_child:
                self.left_child.fill(overflow / 2)
            if self.right_child:
                self.right_child.fill(overflow / 2)
        return overflow


def test(cases, solution_classes):
    for Solution_class in solution_classes:
        print('---')
        for poured, query_row, query_glass in cases:
            solution = Solution_class()
            print(solution.champagneTower(poured, query_row, query_glass))


test([
    # (1, 1, 1),  # 0.0
    # (2, 1, 1),  # 0.5
    # (4, 2, 1),  # 0.5
    # (4, 2, 0),  # 0.25
    # (100000009, 33, 17)  # 1
    #
    # , (0.6, 1, 1)
    # , (0.8, 1, 1)
    (0.9, 2, 0)
], [Solution, Solution1])
