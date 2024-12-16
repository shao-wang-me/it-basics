from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        K = {}
        for k in knowledge:
            K[k[0]] = k[1]

        print(K)

        result = ''

        q = ''

        for c in s:
            if c == '(':
                q += c
            elif c == ')':
                q += c
                result += K[q[1:-1]] if q[1:-1] in K else '?'
                q = ''
            elif q:
                q += c
            else:
                result += c

        print(result)

        return result


solution = Solution()
solution.evaluate('(name)is(age)yearsold', [["name", "bob"], ["age", "two"]])
solution.evaluate('hi(name)', [["a", "b"]])
solution.evaluate('(a)(a)(a)aaa', [["a", "yes"]])
solution.evaluate('(a)(b)', [["a", "b"], ["b", "a"]])
