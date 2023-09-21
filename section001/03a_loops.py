# 03a - Loops

# >>> list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> list(range(5, 10))
# [5, 6, 7, 8, 9]
# >>> list(range(5, 25, 6))
# [5, 11, 17, 23]
# >>> list(range(100, 2, -9))
# [100, 91, 82, 73, 64, 55, 46, 37, 28, 19, 10]
# >>> list(range(101, 2, -9))
# [101, 92, 83, 74, 65, 56, 47, 38, 29, 20, 11]

# infinite loop (x is always less than 10)

# x = 0
# while x < 10:
#     print(x)
#     x -= 1

print('For loop over a string:')
for letter in 'CSCI1030U':
    print(letter)

# Coding Exercise 03a.1

import math

x = 1.0
num_terms = 100
estimate = 0.0

for n in range(num_terms):
    term = x ** n / math.factorial(n)
    estimate += term 

print(f'{estimate = }')

# Coding Exercise 03a.2

x = 2

lower = 0.0
upper = x
guess = (lower + upper) / 2
while abs(guess ** 2 - x) >= 0.00000000001:
    print(f'  guess = {guess}')
    if guess ** 2 < x:
        # our guess is too low
        lower = guess
    elif guess ** 2 > x:
        # our guess is too high
        upper = guess

    guess = (lower + upper) / 2

print(f'The square root of {x} is {guess}')


# hacker's corner

squares = (n**2 for n in [2,4,6,8,10])
for x in squares:
    print(x)
