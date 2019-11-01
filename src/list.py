from collections import deque
import random

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana', 4)

fruits.reverse()

fruits.append('grape')

fruits.sort()

fruits.pop()

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")

queue.popleft()

squares = []

for x in range(10):
    squares.append(x ** 2)

print(squares)

a = [20, 40, 60]
id(a)

b = a + [80]  # 地址发生了变化，创建了一个新的对象
id(b)

# extend()
a.extend([100])
id(a)
print(a)  # [20, 40, 60, 100]

# insert
a.insert(2, 10)
print(a)  # [20, 40, 10, 60, 100]

# 乘法扩展
b = a * 3
print(b)  # [20, 40, 10, 60, 100, 20, 40, 10, 60, 100, 20, 40, 10, 60, 100]

# del
del b[1]
print(b)

# pop
b.pop()
print(b)  # [20, 10, 60, 100, 20, 40, 10, 60, 100, 20, 40, 10, 60]

# remove
b.remove(10)
print(b)  # [20, 60, 100, 20, 40, 10, 60, 100, 20, 40, 10, 60]

# len
print(len(b))

# index
print(b.index(100))
print(b.index(100, 5))

# count
print(b.count(20))

# in
print(20 in b)

# not in
print(20 not in b)

# slice
print(b[:])
print(b[2::2])
print(b[::-1])

#

for x in b:
    print(x)

# sort
b.sort()
print(b)
b.sort(reverse=True)
print(b)

# 乱序
random.shuffle(b)
print(b)

# sorted  不修改原对象 新建另一个对象
c = sorted(b)
print(c)
print(c is b)

# reverse
b.reverse()
print(b)

# reversed
c = reversed(b)  # 返回一个迭代对象，只能用一次
print(list(c))  # [40, 60, 10, 100, 10, 100, 20, 20, 40, 20, 60, 60]
print(list(c))  # []

# max min sum
max(b)
min(b)
sum(b)



