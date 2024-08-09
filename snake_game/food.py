from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.shape('circle')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.random_x = randint(-300, 300)
        self.random_y = randint(-300, 300)
        self.goto(self.random_x, self.random_y)