from turtle import Turtle, Screen
import random

# function to draw each shape
def draw_shape():
    # for loop to start with 3 (sides) and end with 10 (sides)
    for num in range(3, 11):
        # creating each color using RGB scale
        color_1 = random.randrange(0, 256)
        color_2 = random.randrange(0, 256)
        color_3 = random.randrange(0, 256)
        # angle of each shape is 360 divided by the number of sides
        angle = 360 / num
        # set colormode to 255 so RGB numbers will go from 0 to 255
        screen.colormode(255)
        # actually setting the colors to the turtle
        timmy.color(color_1, color_2, color_3)
        # moving the turtle according to the number of sides and angle
        for sides in range(num):
            timmy.forward(100)
            timmy.right(angle)


# setting the object timmy to the module Turtle
timmy = Turtle()
# creating and setting the screen
screen = Screen()
# function call for draw_shape
draw_shape()
# screen will not close until clicked by user
screen.exitonclick()
