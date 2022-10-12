STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle, Screen

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.setposition(STARTING_POSITION)
        
    def check_where(self):
        if round(self.ycor()) == FINISH_LINE_Y:
            self.setposition(STARTING_POSITION)
            return True
    
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        
        

