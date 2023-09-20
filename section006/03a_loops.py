# 03a - Loops

# infinite loop (x is always less than 10)

# x = 0
# while x < 10:
#     print(f'{x} is small')
#     x -= 1

print('While loop:')
x = 0
while x < 10:
    print(f'{x} is small')
    x += 1

print('For loop')
for x in range(0, 10, 1): # [0,1,2,3,4,5,6,7,8,9]
    print(f'{x} is small')

print('For loop (non-one increment):')
for x in range(15, 99, 7):
    print(f'{x} is small')

print('For loop (backwards):')
for x in range(100, 87, -1):
    print(f'{x} is small')


# Coding Exercise 03a.1

import math

x = 1.0
num_reps = 100
estimate = 0.0
for n in range(0, num_reps):
    term = x ** n / math.factorial(n)
    estimate += term 

print(f'{estimate = }')
