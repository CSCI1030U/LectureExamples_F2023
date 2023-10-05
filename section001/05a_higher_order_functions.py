# 05a - Higher-order Functions

def c(x, y):
    print(f'the c function was called with args {x} and {y}')
    return

def b(factor):
    print(f'the b function was called with arg {factor}')
    c(2, 3)

def a():
    print('the a function was called')
    b(1.5)
    return 'CSCI1030U'

result = a()
print(f'{result = }')

# map

names = ['Rhonda', 'Tyler', 'Aaron', 'Li']
name_lengths = map(len, names)
print(f'{list(name_lengths) = }')

names = ['Rhonda', 'Tyler', 'Aaron', 'Li']
first_letters = map(lambda name: name[0], names)
print(f'{list(first_letters) = }')

# reduce

from functools import reduce 

def mult(x, y):
    return x * y 

product = reduce(mult, [1,2,3,4,5])
print(f'{product = }')

# Coding Exercise 05a.1

invoice_items = [
    {'item_price': 9.99, 'quantity': 35},
    {'item_price': 799.99, 'quantity': 1},
    {'item_price': 4.99, 'quantity': 22},
]

def calculate_item_subtotal(previous_sum, current_item):
    return previous_sum + (current_item['item_price'] * current_item['quantity'])

subtotal = reduce(calculate_item_subtotal, invoice_items, 0.0)
print(f'{subtotal = }')

# filter

def is_passing_grade(mark):
    return mark >= 50.0

marks = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
passing_marks = filter(is_passing_grade, marks)
print(f'{list(passing_marks) = }')
