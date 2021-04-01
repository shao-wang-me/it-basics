class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        # 1 [1]
        # 2 [2]
        # 3 [3]
        # 4 [2,2]
        # 5 [3,2]
        # 6 [3,3]
        # 7 [3,2,2]
        # 8 [3,3,2]
        # 9 [3,3,3]
        # 10 [3,3,2,2]

        if primeFactors <= 3:
            return primeFactors
        mod = 10 ** 9 + 7
        if primeFactors % 3 == 0:
            return pow(3, (primeFactors // 3), mod) % mod
        if primeFactors % 3 == 1:
            return pow(3, (primeFactors // 3 - 1), mod) * 4 % mod
        if primeFactors % 3 == 2:
            return pow(3, (primeFactors // 3), mod) * 2 % mod

solution = Solution()
print(solution.maxNiceDivisors(1))
print(solution.maxNiceDivisors(2))
print(solution.maxNiceDivisors(3))
print(solution.maxNiceDivisors(4))
print(solution.maxNiceDivisors(5))
print(solution.maxNiceDivisors(8))
print(solution.maxNiceDivisors(10))
print(solution.maxNiceDivisors(11))
print(solution.maxNiceDivisors(10 ** 6))
print(solution.maxNiceDivisors(10 ** 9))
