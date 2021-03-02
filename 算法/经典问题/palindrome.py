def palindrome_1(string):
    # 两头夹逼
    l, r = 0, len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True


def palindrome_2(string):
    # 中心扩展
    l = (len(string) - 1) // 2
    r = l if len(string) % 2 == 1 else l + 1
    while l >= 0:
        if string[l] != string[r]:
            return False
        l -= 1
        r += 1
    return True


def check_palindrome(f):
    print('>> ' + f.__name__ + '()')
    print(f('abcba'))
    print(f('abccba'))
    print(f(''))
    print(f('a'))
    print(f('abc'))
    print(f('world'))
    print('---')


check_palindrome(palindrome_1)
check_palindrome(palindrome_2)


def check_sub_palindromes(string):
    n = len(string)
    result = []
    for i in range(n):
