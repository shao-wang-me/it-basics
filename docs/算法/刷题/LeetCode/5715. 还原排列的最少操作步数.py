class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))

        def get_new_perm(old):
            return [old[i // 2] if i % 2 == 0 else old[n // 2 + (i - 1) // 2] for i in range(n)]

        count = 1
        new = get_new_perm(perm)
        while perm != new:
            # print(perm, new)
            new = get_new_perm(new)
            count += 1

        print(count)

        return count


solution = Solution()

solution.reinitializePermutation(2)
solution.reinitializePermutation(4)
solution.reinitializePermutation(6)
solution.reinitializePermutation(100)
solution.reinitializePermutation(1000)
