from turtle import Turtle


START_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create()
        self.snake_head = self.snake[0]

    def create(self):
        for position in START_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)


    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)


        self.snake_head.forward(MOVING_DISTANCE)

    def extend_snake(self):
        self.add_snake(self.snake[-1].position())

    def reset_game(self):
        for segment in self.snake:
            segment.goto(1000,1000)
        self.snake.clear()
        self.create()
        self.snake_head = self.snake[0]


    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(180)
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270)
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(0)
