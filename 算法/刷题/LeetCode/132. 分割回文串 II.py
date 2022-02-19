# 132. 分割回文串 II

# TODO Not done!

from math import inf


class Solution:

    def minCut(self, s: str) -> int:
        # 和《分割回文串》类似，但是因为s.lenth最大到2000，用之前的方法会超时
        # 总体方法可能其实是类似的，只是递归的时候不需要返回所有的，而是子字符串的答案
        # 再加上记忆即可
        # 可以说是DP
        n = len(s)
        if n <= 1:
            return 0
        mem = [[1 if i == j else -1 for i in range(n)] for j in range(n)]
        mem2 = [[inf] * n for _ in range(n)]

        def is_palindrome(i, j):
            if not i <= j:
                raise Exception
            if mem[i][j] == -1:
                if i + 1 == j:
                    mem[i][j] = 1 if s[i] == s[i] else 0
                else:
                    mem[i][j] = 1 if (is_palindrome(i + 1, j - 1) and s[i] == s[j]) else 0
            return mem[i][j] == 1

        def min_cut_recursive(start, end):
            if start == end:
                return 0
            # 判断所有头部回文的可能性
            i = end
            while i > start:
                if is_palindrome(start, i):
                    if i + 1 == end:
                        mem2[start][i] = 1
                    else:
                        mem2[start][i] = min(mem2[start][i], min_cut_recursive(i + 1, end - 1) + 1)
                i -= 1
            return mem2[start][end]

        return min_cut_recursive(0, n - 1)


def test(s):
    solution = Solution()
    print(solution.minCut(s))


test('aab')
test('ab')
test('aa')
test('a')
# test('12345678909876543211234567890')
