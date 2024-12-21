import turtle as t

tom = t.Turtle()
jerry = t.Screen()


def tom_forward():
    tom.forward(10)

def tom_backward():
    tom.backward(10)

def tom_turn_counter_clockwise():
    tom.left(10)

def tom_turn_clockwise():
    tom.right(10)

def clear_screen():
    tom.reset()

jerry.onkey(tom_forward, "w")
jerry.onkey(tom_backward, "s")
jerry.onkey(tom_turn_counter_clockwise, "a")
jerry.onkey(tom_turn_clockwise, "d")
jerry.onkey(clear_screen, "c")

jerry.listen()

jerry.exitonclick()