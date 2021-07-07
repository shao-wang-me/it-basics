class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = []
        curr_num = ''
        for c in word + 'a':
            if c.isdigit():
                curr_num += c
            else:
                if curr_num:
                    nums.append(curr_num)
                    curr_num = ''

        print(nums)

        nums = set(int(x) for x in nums)

        print(nums)

        return len(nums)



solution = Solution()
solution.numDifferentIntegers('a123bc34d8ef34')
solution.numDifferentIntegers('leet1234code234')
solution.numDifferentIntegers('a1b01c001')
