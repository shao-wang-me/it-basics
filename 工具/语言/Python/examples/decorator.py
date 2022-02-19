# 装饰器就是一个返回一个函数的函数


def print_out(func):
    def f(*args, **kwargs):
        print(func(*args, **kwargs))

    return f


@print_out
def add(x, y):
    return x + y


def add1(x, y):
    return x + y


print(add)
add(1, 2)

# 和用@print_out时等价的
print_out(add1)(1, 2)


# 带参数的装饰器
# 作者：三眼鸭的编程教室
# 链接：https://www.zhihu.com/question/26930016/answer/1904166977
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

def info(value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(value)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@info('456')
def say_hello():
    print('同学你好')


say_hello()

# 也能用类实现装饰器
# 也有装饰类的装饰器
