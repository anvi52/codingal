import turtle

# creating canvas
turtle.Screen().bgcolor("Orange")

SC = turtle.Screen()
SC.setup(400, 300)

turtle.title("welcome to turtle window")

# turtle object creation
board = turtle.Turtle()

# creating a Square
for i in range(4):
    board.forward(100)
    board.left(90)
    i= 1+1
turtle.done()