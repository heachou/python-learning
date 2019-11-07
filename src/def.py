import time
import math


# 测试函数的定义和使用

def print_max(a, b):
    """比较两个指的大小"""
    if a > b:
        print(a)
    else:
        print(b)


def add(a, b):
    return a + b


def run_time():
    start = time.time()
    sqrt = math.sqrt
    for i in range(10000000):
        sqrt(20)
    end = time.time()
    print('耗时{0}'.format((end - start)))


help(print_max.__doc__)

print_max(10, 20)
print_max(20, 10)
print_max(30, 20)

c = add(1, 2)
print(c)

run_time()
