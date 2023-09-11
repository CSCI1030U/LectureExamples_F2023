import turtle 

window = turtle.Screen()

my_turtle = turtle.Turtle()

# move into position for the 'R'
my_turtle.penup()
my_turtle.right(180)
my_turtle.forward(300)
my_turtle.left(90)
my_turtle.forward(250)
my_turtle.right(180)

# draw the 'R'
my_turtle.pendown()
my_turtle.forward(500)
my_turtle.right(90)
my_turtle.forward(250)
my_turtle.right(90)
my_turtle.forward(250)
my_turtle.right(90)
my_turtle.forward(250)
my_turtle.left(135)
my_turtle.forward(350)

# move into position for the 'F'
my_turtle.penup()
my_turtle.left(45)
my_turtle.forward(100)

# draw main part of the 'F'
my_turtle.pendown()
my_turtle.left(90)
my_turtle.forward(500)
my_turtle.right(90)
my_turtle.forward(250)

# move into position to draw the middle bar of the 'F'
my_turtle.penup()
my_turtle.right(180)
my_turtle.forward(250)
my_turtle.left(90)
my_turtle.forward(250)
my_turtle.left(90)

# draw the middle bar of the 'F'
my_turtle.pendown()
my_turtle.forward(200)

window.mainloop()
