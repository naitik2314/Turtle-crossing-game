import random
import time
from turtle import Screen
from car import Car
from score import Score
from turtle_player import Player

#Some constants
speed = 10

#Screen Setup
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('skyblue')
screen.title('Turtle Crossing')
screen.tracer(0)

#Setting up the screen to listen
screen.listen()

#Player setup
player = Player()

#Player moving
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_up, "Up")

#Intializing the score board
score = Score()

#Game loop
game_is_on = True
player_too_close = False

#Initializing an empty array to store all of the cars we make
cars = []

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 5) == 1:
        car = Car(speed)
        cars.append(car)

    for car in cars:
        car.move_forward()

        if player.distance(car) < 22:
            score.game_over()
            game_is_on = False
        
        if player.ycor() == 280:
            score.level_up()
            player.leveled_up()
            speed += 10
                
screen.exitonclick()

