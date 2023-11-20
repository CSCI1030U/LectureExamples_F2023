# 09b Algorithm Strategies

# Coding Exercise 09b.1
def dc_search(values, to_find):
    # base case
    if len(values) == 0:
        return False
    
    if len(values) == 1:
        return to_find == values[0]

    # divide (the list in half)
    middle = len(values) // 2
    first = values[:middle]
    last = values[middle:]

    # conquer
    first_result = dc_search(first, to_find)
    last_result = dc_search(last, to_find)

    # combine
    return first_result or last_result

print(f'{dc_search([4,1,3,5,2], -1) = }')
print(f'{dc_search([4,1,3,5,2], 2) = }')
print(f'{dc_search([4,1,3,5,2], 4) = }')
print(f'{dc_search([4,1,3,5,2], 5) = }')
print(f'{dc_search([2], -1) = }')
print(f'{dc_search([], -1) = }')

# Coding Exercise 09b.2

# TODO

# Coding Exercise 09b.3
def dp_fib(n):
    solutions = [0, 1]

    if n < 2:
        return solutions[n]
    
    for i in range(2, n + 1):
        next_fib = solutions[i - 1] + solutions[i - 2]
        solutions.append(next_fib)
    
    return solutions[n]

print(f'{dp_fib(0) = }')
print(f'{dp_fib(1) = }')
print(f'{dp_fib(2) = }')
print(f'{dp_fib(3) = }')
print(f'{dp_fib(4) = }')
print(f'{dp_fib(120) = }')
