import turtle as t
import random

jerry = t.Screen()
jerry.setup(width=500, height=400)
color = ['red', 'blue', 'green', 'purple','orange']
jerry.bgcolor('black')
def move_turtle(turtle, steps):
    turtle.forward(steps)
show = t.Turtle()
turtles_list = []

def turles():
    y = -70
    for i in range(len(color)):
        create_turtle = t.Turtle('turtle')
        create_turtle.color(color[i])
        create_turtle.penup()
        create_turtle.goto(-230, y)
        y += 30
        turtles_list.append(create_turtle)
    if user_guess:
        is_race_on = True

    while is_race_on:
        for turtle in turtles_list:

            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_guess:
                    print(f"You've won! The {winning_color} turtle is the winner!")

                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")


            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


user_guess = jerry.textinput(title="Choose your bet", prompt="Which turtle will win the race?")
turles()

jerry.exitonclick()
