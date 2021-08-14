# List

l = [1, 2, 3]

for x in l:
  print(x)

for i, x in enumerate(l):
  print(i, x)

# 倒过来

print(l[::-1])

print(
  list(
    reversed(l)
  )
)


# Dict

d = {'a': 1, 'b': 2, 'c': 3}

for k in d:
  print(k)

for k, v in d.items():
  print(k, v)

for k in d.keys():
  print(k)

for v in d.values():
  print(v)