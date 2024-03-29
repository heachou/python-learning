# 列表属于可变序列 元组属于不可变序列，不能修改元组中的元素，因此，元组没有增加元素、修改元素、删除元素的功能

# create

a = 10, 20, 30
print(type(a))
b = tuple('abc')
print(type(b))
print(b)  # ('a', 'b', 'c')

# zip
a = [10, 20, 30]
b = [30, 40, 50, 60]
c = zip(a, b)
print(c)  # <zip object at 0x03607760>
print(list(c))  # [(10, 30), (20, 40), (30, 50)]

s = (x * 2 for x in range(5))
print(tuple(s))  # (0, 2, 4, 6, 8)
print(tuple(s))  # () 只能用一次

s = (x * 2 for x in range(6))

print(s.__next__())  # 0
print(s.__next__())  # 2
print(s.__next__())  # 4
