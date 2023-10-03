# 05a - Higher-order Functions

# hacker's corner (stack visualization)

def c(first, last):
    print(f'c was called with the arguments {first} and {last}')

def b(x):
    print(f'b was called with the argument {x}')
    c('Michael', 'Jackson')

def a():
    print('a was called')
    b(1)
    return True

result = a()

# map

def square(x):
    return x ** 2

squares = map(square, [1,2,3,4,5,6,7,8,9,10])
print(f'{list(squares) = }')

squares = map(lambda x: x ** 2, [1,2,3,4,5,6,7,8,9,10])
print(f'{list(squares) = }')

# reduce

from functools import reduce 

def mult2(a,b):
    return a * b

product = reduce(mult2, [1,2,3,4,5])
print(f'{product = }')

product = reduce(lambda a,b: a * b, [1,2,3,4,5])
print(f'{product = }')

# filter 

def is_passing(mark):
    return mark >= 50.0

passing_marks = filter(is_passing, [45.0, 55.0, 80.0, 30.0, 50.0])
print(f'{list(passing_marks) = }')

passing_marks = filter(lambda m: m >= 50.0, [45.0, 55.0, 80.0, 30.0, 50.0])
print(f'{list(passing_marks) = }')
