name = 'Randy'
# name = input('What is your name? ')
print('Hello', name, '!')
greeting = 'Hello' + name + '!'
print(greeting)
print('Hello', name, '!', sep = 'pizza', end = 'END\n')
print('next line')

print(f'Hello there, {name}.  I said {greeting} before.')
print(f'8 + 3 = {8 + 3}')

class_average = 71.5 # <- snake case, camel case: classAverage

print(f'{name = }')
name_type = type(name)
print(f'{name_type = }')

# Coding Exercise 01b.2

import turtle 

window = turtle.Screen()

jim = turtle.Turtle()

jim.pendown()

jim.forward(50)
jim.right(90)
jim.forward(60)
jim.right(90)
jim.forward(70)
jim.right(90)
jim.forward(80)
jim.right(90)
jim.forward(90)

window.mainloop()