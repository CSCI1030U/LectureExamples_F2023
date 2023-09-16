# 02b - Conditionals

age = 18
if age < 5:
    print('Sorry, no Nintendo Switch for you')

age = 5
if age < 7:
    print('You have to be 5 to use this.')
else:
    print('Go ahead and use the Switch')

age = 10
if age < 5:
    print('You cannot use this device.')
elif age < 8:
    print('You can play Minecraft')
else:
    print('Play what you like')

# Coding Exercise 02b.1

num1 = int(input('Enter the first number:  '))
num2 = int(input('Enter the second number: '))

# if num1 % 2 == 0:
#     # num1 is an even number
#     if num2 % 2 == 0:
#         # num2 is an even number
#         print('Both numbers are even')

if (num1 % 2 == 0) and (num2 % 2 == 0):
    # num2 is an even number
    print('Both numbers are even')

# Coding Exercise 02b.2

health_points = -2

if health_points <= 0:
    health_points = 0
    is_dead = True 
else:
    is_dead = False

print(f'{health_points = }')
print(f'{is_dead = }')

# hacker's corner


even_or_odd = 'even' if (num2 % 2 == 0) else 'odd'
print(f'The number {num2} is {even_or_odd}')
print(f'The number {num2} is {even_or_odd}')
print(f'The number {num2} is {even_or_odd}')
print(f'The number {num2} is {even_or_odd}')
print(f'The number {num2} is {even_or_odd}')
print(f'The number {num2} is {even_or_odd}')
print(f'The number {num2} is {even_or_odd}')
print(f'The number {num2} is {even_or_odd}')

