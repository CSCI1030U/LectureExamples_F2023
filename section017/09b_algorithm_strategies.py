# 09b Algorithm Strategies

def d_and_c_search(values, to_find):
    # base cases
    if len(values) == 0:
        return False 

    if len(values) == 1:
        return to_find == values[0]    

    # divide the list in half
    first = values[0:len(values)//2]
    last = values[len(values)//2:]

    # conquer (recursively search the two list halves)
    first_result = d_and_c_search(first, to_find)
    last_result = d_and_c_search(last, to_find)

    # combine either in the 1st half or 2nd half
    return first_result or last_result

print(f'{d_and_c_search([5,2,3,1,4], -1) = }')
print(f'{d_and_c_search([5,2,3,1,4], 5) = }')
print(f'{d_and_c_search([5,2,3,1,4], 1) = }')
print(f'{d_and_c_search([5,2,3,1,4], 4) = }')
print(f'{d_and_c_search([4], 4) = }')
print(f'{d_and_c_search([], 4) = }')

# Coding Exercise 09b.2

# later

# Coding Exercise 09b.3

def dp_fib(n):
    solutions = [0,1]
    if n <= 1:
        return solutions[n]
    
    for i in range(2, n + 1):
        new_fib = solutions[i - 1] + solutions[i - 2]
        solutions.append(new_fib)
    
    return solutions[n]

print(f'{dp_fib(80) = }')