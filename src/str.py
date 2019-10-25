# 字符串学习
# Unicode


print(ord('A'))  # 65
print(ord('高'))  # 39640

print(chr(66))  # B

# 引号创建字符串
# 创建多行字符串

a = """
 this is multiple line
 this is multiple line
 this is multiple line
"""
print(a)
print(len(a))

# 转义字符
# \(在行尾时) 续行符
# \\ \
# \' '
# \* *
# \b 退格符 Backspace
# \n 换行
# \t 横向制表符
# \r 回车

a = 'i\nlove\nyou'

print(a)

# 字符串拼接
# + 或空格

a = 'hell' + 'o'
print(a)
a = 'hello' 'test'
print(a)

# 字符串复制
a = 'hello ' * 3
print(a)

# 不换行打印
print("test1", end='')
print("test2", end='$$$')
print("test3", end='\n')

# 从控制台读取字符串
# my_name = input("请输入name:")
# print(my_name)

# str 转换为字符串
print(type(str(5.13)))  # <class 'str'>
print(str(True))  # True

# []
a = 'abcd'
print(a[0])  # a
print(a[-1])  # d

# replace 替换字符串
a = 'hello'
b = a.replace('l', 'u')
print(a)  # hello
print(b)  # heuuo

# slice 切片
a = 'abcdefg'
print(a[1:5])  # bcde
print(a[1:5:2])  # bd
print(a[:])  # abcdefg
print(a[2:])  # cdefg
print(a[:2])  # ab
print(a[-3:])  # efg
print(a[::-1])  # gfedcba 倒序

a = 'to be or not to be'
b = a.split()
print(a.split())
print('$'.join(a))


