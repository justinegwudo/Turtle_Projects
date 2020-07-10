import turtle
import random

justin = turtle.Turtle()
justin.color("black")
justin.pensize(10)
justin.shape("turtle")

colors = ["red", "blue", "green", "yellow", "black"]


def left():
    justin.setheading(180)
    justin.forward(100)


def right():
    justin.setheading(0)
    justin.forward(100)


def up():
    justin.setheading(90)
    justin.forward(100)


def down():
    justin.setheading(270)
    justin.forward(100)


def clickleft(x, y):
    justin.color(random.choice(colors))


def clickright(x, y):
    justin.stamp()


# listen for user input
turtle.listen()

# listen for click
turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)

# listen, we are looking for arrow key input
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")

turtle.mainloop()
