from turtle import Turtle

PEDDLE_STEP = 40

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(position)
        self.peddal_step = PEDDLE_STEP

    def go_up(self):
        new_y = self.ycor() + self.peddal_step
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.peddal_step
        self.goto(self.xcor(), new_y)
