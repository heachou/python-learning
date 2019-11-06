import math

year = 2019
event = 'Referendum'

print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495

print(yes_votes)
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

s = 'Hello, world.'
str(s)

repr(s)

str(1 / 7)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))

print(f'The value of pi is approximately {math.pi:.16f}.')

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

value = ('the answer', 42)
s = str(value)  # convert the tuple to string
print(s)
