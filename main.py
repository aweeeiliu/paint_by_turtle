# import colorgram
#
# colours = colorgram.extract('hirst-painting.jpg', 20)
# rgb_color = []
#
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

import turtle
from turtle import Turtle, Screen
import random

color_list = [(238, 252, 245), (248, 231, 27), (202, 12, 30), (35, 91, 186), (232, 229, 4), (232, 149, 48), (197, 68, 22), (212, 13, 9), (35, 31, 152), (49, 220, 60), (241, 46, 151), (20, 22, 53), (14, 208, 224), (75, 9, 53), (17, 154, 18), (55, 26, 13), (80, 193, 223)]

tim = Turtle()
screen = Screen()
turtle.colormode(255)
tim.shape('circle')
tim.speed(10)
tim.penup()
tim.hideturtle()
tim.setposition(-180.0, -180.0)

def stamping():
    tim.stamp()
    tim.fd(40)
    tim.color(random.choice(color_list))

def move_up():
    tim.setposition(-180.0, tim.ycor() + 40.0)

for i in range(10):
    move_up()
    for j in range(10):
        stamping()

screen.exitonclick()
