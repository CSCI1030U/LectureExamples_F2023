# 03a - Loops

# infinite loop

# x = 0
# while x < 10:
#     print(f'{x} is small.')
#     x = x - 1

print('While loop:')
num = 5
while num <= 10:
    print(num)
    num += 1

print('For loop:')
for num in [5,6,7,8,9,10]:
    print(num)

print('For loop using range():')
for num in range(5, 11):
    print(num)

print('For loop with step size:')
for num in range(10, 200, 15):
    print(num)

print('For loop with negative step size:')
for num in range(200, 10, -15):
    print(num)

# Coding Exercise 03a.1

import math

estimate = 0
num_reps = 100
x = 1.0
for n in range(num_reps):
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
