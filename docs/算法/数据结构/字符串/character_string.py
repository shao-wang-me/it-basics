def prefix_function(s: str) -> list[int]:
    pi = [0]
    for i in range(1, len(s)):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi.append(j)

    return pi


assert prefix_function('abcabcd') == [0, 0, 0, 1, 2, 3, 0]
assert prefix_function('aabaaab') == [0, 1, 0, 1, 2, 2, 3]
assert prefix_function('ababab') == [0, 0, 1, 2, 3, 4]
assert prefix_function('aabaaab') == [0, 1, 0, 1, 2, 2, 3]
assert prefix_function('hello') == [0, 0, 0, 0, 0]


def kmp(s: str, p: str) -> list[int]:
    pi = [0]
    for i in range(1, len(p)):
        j = pi[i - 1]
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
        pi.append(j)
    indices = []
    j = 0
    for i in range(0, len(s)):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == len(p):
            indices.append(i + 1 - len(p))
            j = 0
    return indices


assert kmp('abc', 'abc') == [0]
assert kmp('hello', 'll') == [2]
assert kmp('aaaaa', 'bba') == []
assert kmp('', '') == []
assert kmp('ababababa', 'ab') == [0, 2, 4, 6]
