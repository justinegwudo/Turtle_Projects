import turtle
from turtle import Screen

screen = Screen()
t = turtle.Turtle()

t.speed(-1)


def dragging(x, y):
    # using .ondrag(None) remove the glue the links it to the library, allowing it to move on other parameter
    # stop turtle from going to previous position
    t.ondrag(None)
    # Change the turtle's head postion to my direction
    t.setheading(t.towards(x, y))
    # Draw a line (.listen feeds it mouse positon)
    t.goto(x, y)
    t.ondrag(dragging)


def clickright():
    t.clear()


def main():
    turtle.listen()

    t.ondrag(dragging)

    turtle.onscreenclick(clickright, 3)

    screen.mainloop()


main()
