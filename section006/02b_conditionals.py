# 02b - Conditionals

age = 18
if age < 5:
    print('You are too young for Pokemon.')

# age = 2
if age < 7:
    print('You are too young to play Pokemon.')
else:
    print('Go ahead and play!')

age = 48
if age < 5:
    print('Pokemon is too advanced for you.')
elif age < 40:
    print('You can play Pokemon')
else:
    print('Have you thought about candy crush?')

# exercise 02b.1

# num1 = int(input('Enter the first number:  '))
num1 = 2
# num2 = int(input('Enter the second number: '))
num2 = 3

if (num1 % 2 == 0) and (num2 % 2 == 0):
    print('Both numbers are even')

# coding exercise 02b.2

health_points = -2

if health_points <= 0:
    is_dead = True 
    health_points = 0
else:
    is_dead = False

print(f'{health_points = }')
print(f'{is_dead = }')

# coding challenge 02b.1 

mark = 40

if mark >= 0 and mark < 50:
    letter_grade = 'F'
elif mark >= 50 and mark < 60:
    letter_grade = 'D'
elif mark >= 60 and mark < 70:
    letter_grade = 'C'
elif mark >= 70 and mark < 80:
    letter_grade = 'B'
elif mark >= 80 and mark <= 100:
    letter_grade = 'A'
print(f'{letter_grade = }')
    
if mark < 50:
    letter_grade = 'F'
elif mark < 60:
    letter_grade = 'D'
elif mark < 70:
    letter_grade = 'C'
elif mark < 80:
    letter_grade = 'B'
elif mark <= 100:
    letter_grade = 'A'
print(f'{letter_grade = }')
    
# hacker's corner

num = 11

if num % 2 == 0:
    status = 'even'
else:
    status = 'odd'

status = 'even' if num % 2 == 0 else 'odd'

print(f'The number {num} is {status}')