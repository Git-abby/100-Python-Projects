# import colorgram
#
#
# color_bank = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     color_bank.append(color_tuple)
#
# print(color_bank)
import turtle as t
import random

t.colormode(255)
color_bank = [(233, 233, 232), (237, 232, 234), (231, 233, 238), (224, 233, 226), (207, 160, 83), (55, 88, 131), (144, 91, 40), (139, 27, 48), (221, 207, 107), (134, 177, 202), (157, 47, 85), (44, 55, 105), (170, 159, 41), (129, 189, 144), (83, 20, 43), (38, 43, 66), (185, 94, 107), (188, 139, 166), (85, 124, 181), (60, 39, 31), (89, 157, 92), (80, 153, 164), (195, 81, 72), (160, 201, 219), (45, 75, 78), (79, 75, 44), (56, 125, 121), (218, 176, 188), (166, 207, 162), (220, 182, 168)]

tom = t.Turtle()
jerry = t.Screen()
tom.speed(0)

x = -225
y = -215

for _ in range(10):

    tom.penup()
    tom.hideturtle()
    tom.goto(x, y)

    for _ in range(10):
        tom.dot(20, random.choice(color_bank))
        tom.forward(50)
    y += 50

jerry.exitonclick()