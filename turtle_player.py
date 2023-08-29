from turtle import Turtle

SPEED = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
    
    def move_up(self):
        self.forward(SPEED)

    def leveled_up(self):
        self.goto(0, -280)