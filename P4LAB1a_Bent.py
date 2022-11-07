import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# Draws the square
for i in (1,2,3,4):
    t.forward(100)
    t.left(90)

# Draws the triangle
for i in (1,2,3):
    t.forward(80)
    t.left(120)

# end commands
win.mainloop()
