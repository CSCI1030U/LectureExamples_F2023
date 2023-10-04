# 05a - Higher-order Functions

def c(x, y):
    print(f'called the c function with args {x} and {y}')

def b(string):
    print(f'called the b function with arg {string}')
    c(1.0, 2.0)

def a():
    print('called the a function')
    b('abcd')
    return -8 

result = a()
print(f'{result = }')

# map

def letter_grade(mark):
    if mark < 50.0:
        return 'F'
    elif mark < 60.0:
        return 'D'
    elif mark < 70.0:
        return 'C'
    elif mark < 80.0:
        return 'B'
    else:
        return 'A'

marks = [40.0, 50.0, 60.0, 70.0, 80.0]
grades = map(letter_grade, marks)
print(f'{list(grades) = }')

# reduce

from functools import reduce 

def product2(a, b):
    return a * b 

marks = [40.0, 50.0, 60.0, 70.0, 80.0]
product_of_marks = reduce(product2, marks)

print(f'{product_of_marks = }')

# filter 

def passing_grade(mark):
    # if mark < 50.0:
    #     return False 
    # else:
    #     return True 
    return mark >= 50.0

marks = [40.0, 50.0, 60.0, 2.0, 70.0, 31.0, 80.0]
passing_marks = filter(passing_grade, marks)
print(f'{list(passing_marks) = }')

passing_marks = filter(lambda mark: mark >= 50.0, marks)
print(f'{list(passing_marks) = }')

# Coding Exercise 05a.1

shopping_cart = [
    {'item_price': 99.99, 'quantity': 10},
    {'item_price': 899.99, 'quantity': 1},
    {'item_price': 14.99, 'quantity': 300},
]

def get_item_subtotal(previous_sum, current_item):
    return previous_sum + (current_item['item_price'] * current_item['quantity'])
subtotal = reduce(get_item_subtotal, shopping_cart, 0)
print(f'{subtotal = }')