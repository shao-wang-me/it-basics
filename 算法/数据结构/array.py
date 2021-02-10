# 创建
# 没法用list作为变量名，因为list是Python保留字
lst = [1, 2, 3, 4, 'hi', {2: 'hello'}]
print(lst[4])

# 改元素
lst[1] = 'cool'
print(lst)

# 尾增
lst.append('good')
lst += ['enough']
print(lst)
# 在现有2前插入，插入的变成2
lst.insert(2, '此处')
lst = lst[0: 2] + ['何方'] + lst[2: -1]
print(lst)

# 拼一个
lst.extend(['远方', '水流'])  # extend的可以是一个可便利的东西，比下面的+=另一个list用处更广
lst += ['♥']
print(lst)

# 移除
lst.append('何方')
lst.remove('何方')  # 只移除第一个该值
print(lst)
lst.pop()  # 移除最后一个
print(lst)
lst.pop(2)  # 也能移除特定index的
print(lst)

# 子list
print(lst[2:5])  # 2 <= index < 5
print(lst[2:5:2])  # 步长为2
print(lst[2:])
print(lst[:4])
print(lst[4:2])  # 反向是不行的
print(list(reversed(lst[2:4])))  # 真想反的话

# 反向
rev_list = list(reversed(lst))
print(rev_list)
# 或者原地反
lst.reverse()
print(lst)

# 清空
lst.clear()
print(lst)

# 计数（给个值）
lst = [1, 2, 3, 4, 21, 3123, 1, 2, 3]
print(lst.count(1))

# 找位置（给个值）
print(lst.index(1))
# 从子list找
print(lst.index(1, 2, -1))  # value[, start[, stop]]

# 排序
lst.sort()
print(lst)
# 反向排序
lst.sort(reverse=True)
print(lst)
# 也可以给一个key函数用于排序
lst = [{'k': 5}, {'k': 3}]
lst.sort(key=lambda d: d['k'])
print(lst)
