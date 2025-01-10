from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()
wall = Turtle()



def draw_wall():
    wall.pensize(15)
    wall.color("white")
    wall.penup()
    wall.goto(-295, -295)
    wall.pendown()
    wall.goto(-295, 295)
    wall.goto(285, 295)
    wall.goto(285, -285)
    wall.goto(-285, -285)

draw_wall()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.right , "Right")
screen.onkey(snake.left , "Left")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.reset_game()
        # scoreboard.game_over()

#     Detect collison with body
    for body in snake.snake[1:]:
        if snake.snake_head.distance(body) < 10:
            snake.reset_game()
            scoreboard.reset()


screen.exitonclick()
