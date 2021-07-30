from turtle import Turtle, Screen
import random


def draw_shape():
    for num in range(3, 11):
        color_1 = random.randrange(0, 256)
        color_2 = random.randrange(0, 256)
        color_3 = random.randrange(0, 256)
        angle = 360 / num
        screen.colormode(255)
        timmy.color(color_1, color_2, color_3)
        for sides in range(num):
            timmy.forward(100)
            timmy.right(angle)


timmy = Turtle()
screen = Screen()
draw_shape()
screen.exitonclick()
