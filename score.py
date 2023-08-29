from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        # self.color("black")
        self.level = 1
        self.write(f"Level: {self.level}", align='center', font=("Arial", 9))

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='center', font=("Arial", 9))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over, final score: {self.level}", align='center', font=("Arial", 12))