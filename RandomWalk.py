import turtle as t
import random

# Function to move the turtle in a random direction and color
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def random_move():
    t.pendown()
    t.color(random_color())
    t.width(random.randint(1, 10))  # Set the width of the pen to a random value between 1 and 5
    t.setheading(random.choice([0, 90, 180, 270]))
    t.forward(38)


# Main code
t.speed(0)
t.shape("turtle")

for _ in range(500):
    random_move()

t.done()
