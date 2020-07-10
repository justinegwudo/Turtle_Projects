import turtle
import os

window = turtle.Screen()

window.title("Justin Egwudo\'s Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# This block creates the paddle on the left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# This block creates the paddle on the right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# This block creates the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


# Create pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B: 0", align="center", font=("courier", 24, "normal"))



# ball movement
ball.dx = 2
ball.dy = -2


# This function move paddle_a up
def paddle_a_up():
    # return y from cordinate from turtle module
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


# function to move paddle_a down
def paddle_a_down():
    # return y from cordinate from turtle module
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)


# This function move paddle_b up
def paddle_b_up():
    # return y from cordinate from turtle module
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


# function to move paddle_b down
def paddle_b_down():
    # return y from cordinate from turtle module
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)


# Collect input
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# game loop
while True:
    # trigger window update
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball boundary +y
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # ball boundary -y
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")


    # ball boundary +x
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    # ball boundary +x
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))




    # Paddle & ball collisions b
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1


# Paddle & ball collisions a
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1