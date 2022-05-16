###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
from turtle import Turtle, Screen

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

tim = Turtle()
screen = Screen()
screen.colormode(255)
y = -250

for _ in range(10):
    tim.penup()
    tim.goto(-180, y)
    tim.pendown()

    for _ in range(10):
        tim.color(random.choice(rgb_colors))
        tim.dot(size=10)
        tim.penup()
        tim.forward(40)
        tim.pendown()
    y += 30

screen.exitonclick()
