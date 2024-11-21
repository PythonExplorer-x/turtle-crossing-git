from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-150, 260)
        self.write(f'Level: {self.score}', align='center', font=('Courier', 24, 'normal'))

    def score_update(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        # self.pendown()
        self.teleport(0, 0)
        # self.showturtle()
        # self.pendown()
        # self.stamp()
        self.color('black')
        self.write('Game Over', align='center', font=('Courier', 44, 'normal'))

