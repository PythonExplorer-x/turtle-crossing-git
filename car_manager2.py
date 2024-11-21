from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green",
          "blue", "purple", "DeepSkyBlue",
          "DeepPink3", "blue4", "cyan"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 3)
        self.color(choice(COLORS))
        self.x_move = -0.04
        # self.y_move = 0.1
        x_random_distance = randint(0, 600)
        x_start = 0
        distance_between_cars_multiplier = randint(-50, 50)
        self.teleport(x_start + x_random_distance, distance_between_cars_multiplier*STARTING_MOVE_DISTANCE)

    def move(self):
        self.penup()
        self.speed('slowest')
        new_x = self.xcor()+self.x_move
        self.goto(new_x, self.ycor())

    def reset_position(self):
        self.color(choice(COLORS))
        x_random_distance = randint(0, 400)
        distance_between_cars_multiplier = randint(-50, 50)
        self.teleport(300 + x_random_distance, distance_between_cars_multiplier*STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.x_move *= 1.3






