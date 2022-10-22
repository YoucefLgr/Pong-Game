from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, i):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(i)

    def up(self):
        if self.ycor() < 240:
            x = self.ycor()+20
            self.goto(self.xcor(), x)

    def down(self):
        if self.ycor() > -240:
            x = self.ycor()-20
            self.goto(self.xcor(), x)








