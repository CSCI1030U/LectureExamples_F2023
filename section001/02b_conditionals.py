# 02b - Conditionals

age = 6
if age < 8:
    print('Sorry, you can only play on the TV')

age = 20
if age < 4:
    print('You are too small to play the Switch')
else:
    print('You can play the switch')

age = 10
if age < 4:
    print('Do you want to watch TV?')
elif age < 8:
    print('You can play Minecraft')
else:
    print('You can play whatever')

# age = 4
# name = 'Logan'
# if age >= 4:
#     if name != 'Logan':
#         print('You can play my switch buddy')

# if age >= 4 and name != 'Logan':
#     print('You can play my switch buddy')

# Coding Exercise 02b.1

# num1 = int(input('Enter the first number:  '))
num1 = 2
# num2 = int(input('Enter the second number: '))
num2 = 4

# if (num1 % 2 == 0):
#     if (num2 % 2 == 0):
#         print('Both numbers are even')

if ((num1 % 2) == 0) and (num2 % 2 == 0):
    print('Both numbers are even')

# Coding Exercise 02b.2

health_points = -5

if health_points <= 0:
    health_points = 0
    is_dead = True 
else:
    is_dead = False

print(f'{health_points = }')
print(f'{is_dead = }')

# hacker's corner

num1 = 7
even_or_odd = 'even' if (num1 % 2 == 0) else 'odd'
message = f'The number {num1} is {even_or_odd}.'
print(message)
