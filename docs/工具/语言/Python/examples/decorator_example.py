def print_out(function):
  print(function(4, 5))

@print_out
def add(x, y):
  return x + y

add(1, 2)