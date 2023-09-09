# name = input('Who are you? ')
name = 'Randy'
print('Hello', name, '!')
print('Hello', name, '!', sep = '|', end = 'END\n')

price = 29.99
cost_string = f'The cost of the item is {price} each, {price * 1.13} with tax.'
print(cost_string)

print(f'as of line 10: {price = }')

# price = 'Teddy bear'  # don't do this
price_type = type(price)
print(f'{price_type = }')

is_in_stock = True    # <- snake case, isInStock (camel case)

# Exercise 01b.2

import turtle 

window = turtle.Screen()

jeremy = turtle.Turtle()
jeremy.pendown()

jeremy.forward(50)
jeremy.right(90)
jeremy.forward(60)
jeremy.right(90)
jeremy.forward(70)
jeremy.right(90)
jeremy.forward(80)
jeremy.right(90)
jeremy.forward(90)
jeremy.right(90)
jeremy.forward(100)
jeremy.right(90)
jeremy.forward(110)
jeremy.right(90)
jeremy.forward(120)
jeremy.right(90)
jeremy.forward(130)
jeremy.right(90)
jeremy.forward(140)
jeremy.right(90)
jeremy.forward(150)

window.mainloop()