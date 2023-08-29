from turtle import Turtle
import random

COLOR = ['orange', 'blue', 'green', 'yellow', 'black', 'red', 'pink']

class Car(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=0.75)
        self.color(random.choice(COLOR))
        self.penup()
        self.goto(random.randint(330, 450), random.randint(-265, 270))
        self.speed('slowest')
        self.speed = speed
        self.setheading(180)
    
    def move_forward(self):
        self.forward(self.speed)
        