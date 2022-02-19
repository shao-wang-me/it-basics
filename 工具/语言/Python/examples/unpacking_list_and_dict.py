xs = [1, 2, 3]

print(xs)
print(*xs)  # 相当于 print(1, 2, 3)




d = {'x': 1, 'y': 2, 'z': 3}

def f(x, y, z):
  return x + y + z

print(f(**d))