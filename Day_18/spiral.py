import turtle as t
import random

tom = t.Turtle()
jerry = t.Screen()
jerry.colormode(255)
# tom.width(2)
tom.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def spiral_square(degree_to_increment, radius):
    num_of_circles = int(360 / degree_to_increment)
    for _ in range(num_of_circles):
        tom.circle(radius)
        tom.color(random_color())
        tom.setheading(tom.heading() + degree_to_increment)

spiral_square(5,100)
jerry.exitonclick()