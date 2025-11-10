import turtle
t = turtle.Turtle()
t.speed(5)
t.color("green")

# draw a circce
t.begin_fill()
t.circle(100)
t.end_fill()

# draw a star
t.penup()
t.goto(-40, 30)
t.pendown()
t.color("yellow")
t.begin.fill()
for i in range(5):
    t.forward(80)
    t.right(144)
t.end_fill()

t.hideturtle()
turtle.done()