# 05b - Recursion

def forever(i):
    print(f'forever {i}')
    forever(i + 1)

# forever(0)

def repeat_n_times_iterative(n, message):
    for i in range(n):
        print(message)

def repeat_n_times(n, message):
    # base case (exit condition)
    if n < 1:
        return 

    # recursive case 
    repeat_n_times(n - 1, message)

repeat_n_times(5, 'CSCI1030U')

# Coding Exercise 05b.1

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

# Coding Exercise 05b.2

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
    # result = myfilter(check, values[1:])
    # if check(values[0]):
    #     result.insert(0, values[0])
    # return result
    if check(values[0]):
        return [values[0]] + myfilter(check, values[1:])
    else:
        return myfilter(check, values[1:])

marks = [64.5, 87.0, 55.5, 94.0, 71.5, 46.0, 100.0]
a_grades = myfilter(lambda mark: mark >= 80.0, marks)
# a_grades should be [87.0, 94.0, 100.0]
print(f'{a_grades = }')

# hacker's corner

def repeat_n_times(n, message):
    # base case (exit condition)
    if n < 1:
        return 

    print(message)

    # recursive case 
    repeat_n_times(n - 1, message)

def repeat_n_times_iterative(n, message):
    for i in range(n, 0, -1):
        print(message)

repeat_n_times_iterative(5, 'CSCI1030U')