# 例子一
def f(a, b=2, *args, **kwargs):
  print(a, b, args, kwargs)

f(1)
f(1, 3)
f(a=1, b=3)
f(1, 3, 4, 5, c=6, d=7)



# 例子二：lambda
h = lambda x: x + 1

print(h(1))



# 例子三：# 用 / 和 * 标记参数
# a 和 b 是仅 positional，不能 a=1 这样
# c 和 d 是 positional 或 keyword 的
# e 和 f 是仅 keyword，只能 e=1 这样
def g(a, b, /, c, d, *, e, f):
  pass
