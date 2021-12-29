from turtle import Turtle, Screen
import color_extract
import random

timmy = Turtle()
timmy.ht()
timmy.pu()
timmy.setposition(-200, -200)
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)
color_list = color_extract.corrected_color_list

for i in range(1, 9):
    for _ in range(8):
        rgb = random.choice(color_list)
        timmy.dot(20, rgb)
        timmy.fd(60)
    timmy.setheading(90)
    timmy.fd(60)
    if i % 2 != 0:
        timmy.setheading(180)
    else:
        timmy.setheading(0)
    timmy.fd(60)

pic = timmy.getscreen()
pic.getcanvas().postscript(file='background.eps')

screen.exitonclick()
