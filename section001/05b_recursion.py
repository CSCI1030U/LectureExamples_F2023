# 05b - Recursion

def forever(n):
    print('forever')
    forever(n + 1)

# forever(0)

def print_n_times(n, message):
    # base case (exit condition)
    if n < 1:
        return

    print(message)

    # recursive case
    print_n_times(n - 1, message)

print_n_times(10, 'CSCI1030U')

def fib(n):
    # base case 
    if n == 0 or n == 1:
        return n 
    
    # recursive case
    return fib(n - 1) + fib(n - 2)

print(f'{fib(0) = }')
print(f'{fib(1) = }')
print(f'{fib(2) = }')
print(f'{fib(3) = }')
print(f'{fib(4) = }')
print(f'{fib(5) = }')
# print(f'{fib(50) = }')

# Coding Exercise 05a.?

def myfilter_iterative(check, values):
    result = []

    for val in values:
        if check(val):
            result.append(val)

    return result

def myfilter(check, values):
    # base case
    if len(values) == 0:
        return []

    # recursive case 
    if check(values[0]):
        return [values[0]] + myfilter(check, values[1:])
    else:
        return myfilter(check, values[1:])


def passing_grade(mark):
    if mark >= 50.0:
        return True 
    else:
        return False 

print(f'{myfilter(passing_grade, [40.0, 55.0, 45.0, 75.0, 25.0, 100.0])}')
