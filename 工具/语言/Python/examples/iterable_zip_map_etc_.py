print(
  list(
    zip(
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    )
  )
)

print(
  list(
    map(lambda x: x + 1, [1, 2, 3])
  )
)

print(
  list(
    filter(lambda x: x % 2 == 0, range(10))
  )
)

print(
  ## any() 判断是否有任何元素
  any([1, 2, 3]),  # True
  any([])  # False
)

from functools import reduce
print(
  # reduce(function, sequence[, initial_value])
  reduce(lambda x, y: x + y, [1, 2, 3]),
  reduce(lambda x, y: x + y, [1, 2, 3], -10)
)