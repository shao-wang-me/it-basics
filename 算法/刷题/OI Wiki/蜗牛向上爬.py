# 蜗牛向上爬

# https://oi-wiki.org/basic/simulate/

# 一只一英寸的蠕虫位于n英寸深的井的底部。它每分钟向上爬u英寸，但是必须休息一分钟才能再次向上爬。在休息的时候，它滑落了d英寸。
# 之后它将重复向上爬和休息的过程。蠕虫爬出井口花费了多长时间？我们将不足一分钟的部分算作一整分钟。如果蠕虫爬完后刚好到达井的顶部，我们也设作蠕虫已经爬出井口。

# 虽然是讲解模拟，但公式解更直接

def climb_simulation(n: float, u: float, d: float) -> int:
    time = 0
    height = 1
    while True:
        height += u
        time += 1
        if height >= n:
            return time
        height -= d
        time += 1


def climb(n: float, u: float, d: float) -> int:
    return int((n - u - 1) // (u - d) * 2 + 1)


print(climb_simulation(5, 2, 1))
print(climb_simulation(10, 3, 1))
print(climb_simulation(5, 2, 1.5))

print('---')

print(climb(5, 2, 1))
print(climb(10, 3, 1))
print(climb(5, 2, 1.5))
