from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time
sc = Screen()
sc.setup(800, 600)
sc.bgcolor("black")
sc.title("Pong")
sc.tracer(0)
right_p = Paddle((350, 0))
left_p = Paddle((-350, 0))
b = Ball()
sc.listen()
sc.onkey(right_p.up, "Up")
sc.onkey(right_p.down, "Down")
sc.onkey(left_p.up, "z")
sc.onkey(left_p.down, "s")

t = True
while t:
    z = ScoreBoard()
    time.sleep(b.spe)
    sc.update()
    if b.ycor() >= 280 or b.ycor() <= -280:
        b.bounce_y()
    b.move()
    if b.xcor() > 320 and right_p.distance(b) < 50 or b.xcor() < -320 and left_p.distance(b) < 50:
        b.bounce_x()
    if b.xcor() > 380:
        b.change_r()
        z.ff()
    if b.xcor() < -380:
        b.change_r()
        z.rr()
sc.exitonclick()

