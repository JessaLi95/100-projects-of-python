from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def w():
    tim.fd(10)


def s():
    tim.bk(10)


def a():
    tim.lt(5)


def d():
    tim.rt(5)


def c():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


screen.listen()
screen.onkey(key="w", fun=w)
screen.onkey(key="s", fun=s)
screen.onkey(key="a", fun=a)
screen.onkey(key="d", fun=d)
screen.onkey(key="c", fun=c)

screen.exitonclick()