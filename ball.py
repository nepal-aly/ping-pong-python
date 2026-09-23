from turtle import Turtle
class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        #self.speed=3
        self.x_move=10
        self.y_move=10
    def speeding(self):
        self.x_move+=5
        self.y_move+=5
    