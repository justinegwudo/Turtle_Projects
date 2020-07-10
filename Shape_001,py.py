# import turtle function
import turtle

# define turtle variable
star = turtle.Turtle()

# set turtle speed
star.speed(20)

# loop to create eye using star
def start_loop():
    for i in range(20):
        star.forward(100)
        star.right(170)




star.color("red", "blue")

star.begin_fill()

start_loop()

star.end_fill()

star.penup()
star.left(-14)
star.forward(100)
star.pendown()

star.color("red", "blue")

star.begin_fill()

start_loop()

star.end_fill()

turtle.setposition(0, 300)
turtle.write("I CAN SEE YOU", move = False, align = "center", font = ("Arial", 30, "bold"))


turtle.done()


