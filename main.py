import turtle as t
import random

timy = t.Turtle()
screen = t.Screen()

t.colormode(255) # for rgp color usage


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timy.pencolor(random_color())
        timy.circle(100)
        # timy.setheading(timy.heading() + size_of_gap)
        timy.left(size_of_gap)


draw_spirograph(7)


screen.exitonclick()


