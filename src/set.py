basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)  # True
print('crabgrass' in basket)  # False

a = set('abracadabra')
print(a)  # {'b', 'r', 'a', 'c', 'd'}

b = set('alacazam')
print(b)  # {'z', 'm', 'l', 'c', 'a'}

print(a - b)  # {'b', 'd', 'r'}
print(a | b)  # {'z', 'm', 'l', 'd', 'c', 'a', 'r', 'b'}
print(a & b)  # {'c', 'a'}
print(a ^ b)  # {'z', 'm', 'l', 'r', 'b', 'd'}
