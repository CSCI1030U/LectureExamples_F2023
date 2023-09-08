# name = input('What is your name? ')
name = 'Randy'
print('Hello', name, '!', sep = '+', end='END\n')
print(f'Hello, {name}!')

print(f'2 + 3 = {2+3}')

# ask the user how old they are, and tell them how old they'll be next year
# age_str = input('How old are you? ')
age_str = '48'
age = int(age_str)
print(f'Next year you will be {age + 1}')

# types

am_i_hungry = True   # <= (snake case) amIHungry (camel case)
aih_type = type(am_i_hungry)
print(f'{aih_type = }')

# Exercise 01b.2

import turtle

window = turtle.Screen()
tortoise = turtle.Turtle()

tortoise.pendown()

tortoise.forward(50)
tortoise.right(90)
tortoise.forward(60)
tortoise.right(90)
tortoise.forward(70)
tortoise.right(90)
tortoise.forward(80)
tortoise.right(90)
tortoise.forward(90)
tortoise.right(90)
tortoise.forward(100)
tortoise.right(90)
tortoise.forward(110)
tortoise.right(90)
tortoise.forward(120)
tortoise.right(90)
tortoise.forward(130)
tortoise.right(90)
tortoise.forward(140)
tortoise.right(90)
tortoise.forward(150)

window.mainloop()