#simple pong in python
# By Dharmendra Bhagat

import turtle
import winsound
wn = turtle.Screen()

wn.title("Pong by @DBhagat")
wn.bgcolor("red")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# paddle A
paddle_a =turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
# paddle B
paddle_b =turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball circle
ball =turtle.Turtle()
ball.speed(0)
ball.shapesize(stretch_len=2, stretch_wid=2)
ball.shape("circle")
ball.color("Navy Blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 1/5
ball.dy = 1/5

# ball Movement(speed)
ball.dx = 0.115
ball.dy = -0.115

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260 )
pen.write("Player A : 0 Player B : 0 ", align="center", font=("Courier ", 28, "normal"))
# Function
def paddle_a_up():
    y =paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y =paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y =paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y =paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
# keybord call

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# main game loop

while True:
    wn.update()

# move ball
    ball.speed(1)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
 # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390 :
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier ", 28, "normal"))
        if (score_a == 10):
            pen.goto(0, 0)
            pen.write("Player A is win the Match", align="center", font=("Courier ", 30, "normal"))
            #pen.clear()
                        #break
    if ball.xcor() < -390 :
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier ", 28, "normal"))
        if (score_b == 10):
            pen.goto(0, 0)
            pen.write("Player B is win the Match", align="center", font=("Courier ", 30, "normal"))


    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350 ) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

