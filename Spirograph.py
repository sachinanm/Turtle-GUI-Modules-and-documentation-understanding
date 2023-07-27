import turtle as t
import random

# Function to move the turtle in a random direction and color
tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


tim.speed("fastest")


def draw_spirograph(size_of_gape):
    for _ in range(int(360 / size_of_gape)):
        tim.circle(100)
        tim.color(random_color())
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gape)


draw_spirograph(5)

t.done()
