from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.shapesize(1, 1)
        x_pos = 0
        y_pos = -280
        self.left(90)
        self.teleport(x_pos, y_pos)

    def go_up(self):
        self.penup()
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        x_pos = 0
        y_pos = -280
        self.teleport(x_pos, y_pos)

