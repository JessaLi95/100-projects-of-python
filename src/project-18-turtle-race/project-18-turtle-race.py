from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
# Place your bet
user_bet = screen.textinput(title="Make your bet", prompt="Which color of turtles will win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:  # the turtle is 40*40
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won, the {winning_color} turtle is the winning turtle")
            else:
                print(f"You lose, the {winning_color} turtle is the winning turtle")
        ran_distance = random.randint(0, 10)
        turtle.fd(ran_distance)

screen.exitonclick()