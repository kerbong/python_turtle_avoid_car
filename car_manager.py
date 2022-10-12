COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2, 0)
        self.penup()
        self.color(COLORS[random.randrange(0,5)])
        where_y = random.randrange(-230, 250)
        self.setpos(320, where_y)
        self.setheading(180)
        
    def move_west(self, speed):
        self.forward(speed)
        
        
