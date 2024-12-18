import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

screen.listen()

scoreboard = Scoreboard()
# Create cars.
all_cars = []  # Contains all cars

# Replace the functionality of the commented out lines with a for loop.
number_of_cars = 12
for car in range(12):
    all_cars.append(CarManager())

# Verify all_cars contains car objects:
for item_number, item in enumerate(all_cars):
    print(f'The object in list[{item_number}] is of the {type(item)=}')

player = Player()
screen.onkeypress(player.go_up, "Up")

while game_is_on:
    screen.update()

    for one_car in all_cars:
        one_car.move()
        if one_car.xcor() < -320:
            one_car.reset_position()

    for this_car in all_cars:
        if player.distance(this_car) < 40:
            scoreboard.game_over()
            screen.update()
            time.sleep(5)
            game_is_on = False

    if player.ycor() > 290:
        scoreboard.score_update()
        player.reset_position()
        for that_car in all_cars:
            that_car.increase_speed()

screen.exitonclick()
