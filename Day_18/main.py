import turtle as t
import random
from color_data import names

tom = t.Turtle()
jerry = t.Screen()
jerry.colormode(255)

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

tom.width(5)
for _ in range(200):
    tom.forward(30)
    tom.color(random_color())
    tom.setheading(random.choice(directions))

