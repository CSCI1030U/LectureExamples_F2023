# Coding Exercise 05a.1

from functools import reduce

invoice_items = [
    {'item_price': 9.99, 'quantity': 10},
    {'item_price': 4.99, 'quantity': 21},
    {'item_price': 849.99, 'quantity': 2},
]

def calculate_item_price(previous_sum, current_item):
    return previous_sum + (current_item['item_price'] * current_item['quantity'])

subtotal = reduce(calculate_item_price, invoice_items, 0)
print(f'{subtotal = }')

# Coding Exercise 05a.2

def myfilter(check, values):
    result = []

    for val in values:
        if check(val):
            result.append(val)

    return result 

marks = [64.5, 87.0, 55.5, 94.0, 71.5, 46.0, 100.0]
a_grades = myfilter(lambda mark: mark >= 80.0, marks)
print(f'{a_grades = }')
# a_grades should be [87.0, 94.0, 100.0]
