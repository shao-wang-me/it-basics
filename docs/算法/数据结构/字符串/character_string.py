def prefix_function(s: str) -> list[int]:
    pi = [0]
    for i in range(1, len(s)):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j -= 1
        if s[i] == s[j]:
            j += 1
        pi.append(j)

    return pi


print(prefix_function('abcabcd'))
