from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ["navy", "spring green", "brown", "green yellow", "dark slate blue", "red", "orange", "pink", "blue",
           "medium purple", "magenta"]


def pattern(shape):
    angle = 360 / shape
    for _ in range(shape):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    pattern(i)
    tim.color(random.choice(colours))

screen = Screen()
screen.exitonclick()
