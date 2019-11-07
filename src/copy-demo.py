import copy

a = [10, 20, [5, 6]]

b = copy.copy(a)

print("a:", a)
print("b:", b)

b.append(30)
b[2].append(7)

print("浅拷贝.............")
print("a:", a)
print("b:", b)

c = [30, 40, [5, 6]]
d = copy.deepcopy(c)

print("c:", c)
print("d:", d)

print("深拷贝.............")

d.append(40)
d[2].append(7)
print("c:", c)
print("d:", d)
