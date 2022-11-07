import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

t.pensize(4)
t.pencolor("blue")

# Draws S initial
t.left(180)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# Moves the pen
t.penup()
t.left(180)
t.forward(100)
t.pendown()

# Draws B initial
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(180)
t.forward(60)
t.right(90)
t.forward(50)
t.right(90)
t.forward(60)
