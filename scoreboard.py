FONT = ("Courier", 20, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    level = 1
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-270, 260)
        
    def write_what(self, what):
        if what == "level":
            self.write(f"Level : {self.level}", font=FONT)
        elif what == "game_over":
            self.write("Game Over", font=FONT)
        
    def level_up(self):
        self.clear()
        self.level += 1
        self.write_what("level")