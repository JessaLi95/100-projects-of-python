from turtle import Turtle, Screen
import random


def random_colour():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.pensize(1)
timmy.speed("fastest")

# Draw shapes
timmy.shape('arrow')
timmy.color('red')

for i in range(3, 11):
    for _ in range(i):
        timmy.rt(360 / i)
        timmy.fd(100)
    random_colour()

# Draw tube map
for _ in range(100):
    timmy.color(random_colour())
    angle_list = [0, 90, 180, 270]
    timmy.setheading(random.choice(angle_list))
    timmy.fd(30)

# Draw spirograph
number_of_circles = 5
for i in range(1, number_of_circles + 1):
    timmy.color(random_colour())
    timmy.circle(50)
    timmy.setheading(360 / number_of_circles * i)


screen.exitonclick()
