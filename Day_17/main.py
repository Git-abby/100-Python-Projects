import turtle as t
from multiprocessing.reduction import send_handle

tom = t.Turtle()

shape_list = ["Triangle", "Square", "Pentagon", "Hexagon", 'Haptagon', "Octagon", "nonagon", "decagon"]
color_list = ["aquamarine", "blue", "BlueViolet", "coral", "cyan", "DeepSkyBlue2", "gold1", "firebrick"]

def draw_shape(deg, num_of_times):
    for i in range(num_of_times):
        tom.forward(100)
        tom.right(deg)

tom.penup()
tom.goto(-50, 200)
tom.pendown()

times = 3
for i in range(len(shape_list)):
    tom.color(color_list[i])
    degree = 360 / times
    draw_shape(degree, times)
    times += 1




jarry = t.Screen()
jarry.exitonclick()

