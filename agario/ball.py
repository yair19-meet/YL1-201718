from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self, x, y, dx, dy, r, color):
        Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)

def move(self, screen_width, screen_height):
    current_x = self.xcor()
    new_x = current_x + self.xcor()
    current_y = self.ycor()
    new_y = current_y + self.ycor()
    right_side_ball = new_x + r
    left_side_ball = new_x - r
    up_side_ball = new_y+ r
    down_side_ball = new_y - r

    self.goto(new_x, new_y)
    
    if right_side_ball > screen_width/2 or left_side_ball < -screen_width/2:
        self.dx = -dx
    if up_side_ball > screen_height/2 or down_side_ball < -screen_height/2:
        self.dy = -dy

        
    
    
    
    
    
