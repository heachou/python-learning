import time

print('a')

# 定义常量
MAX_SPEED = 120

# 解包赋值
a, b, c = 10, 20, 30
# 交换变量的值
c, a, b = a, b, c
print(a, b, c)

# 最基本的数据类型
# 对象由三部分组成  id  type value

# 整型
x = 1
print(type(a))  # <class 'int'>

# 浮点型
y = 1.1
print(type(y))  # <class 'float'>

# 布尔型
z = True
print(type(z))  # <class 'bool'>

# 字符串型
w = 'hello'
print(type(w))  # <class 'str'>

# / 除法  浮点型除法
print(9 / 2)  # 4.5

# // 整型除法
print(9 // 2)  # 4

# % 取余运算
print(9 % 2)  # 1

# ** 幂运算
print(2 ** 3)  # 8

# divmod() 可以同时得到商和余数
print(divmod(9, 2))  # (4,1)

# 类型转换
a = 3.141
print(int(a))  # 3,不改变原始变量的值
print(a)  # 3.141
print(int('1943'))  # int 1943
# print(int('231aa')) error
# print(int('1.121')) error

print(int(True))  # 1
print(2 + 9.1)  # 11.1

# 浮点数
print(314e-2)  # 3.14
print(float(3))  # 3.0
print(round(4.14))  # 4

# 时间
print(time.time())  # 返回以秒为单位

# 逻辑运算符
# or and not
print(True or 22)  # True
print(True and 22)  # 22
print(False or 22)  # 22
print(False and 22)  # False

# is == 的区别
# is 用于判断两个变量引用对象是否为同一个，比较对象的地址
