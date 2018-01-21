from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self, x, y, dx, dy, r, color):
        Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)
        print(self)

    def move(self, screen_width, screen_height):
        current_x = self.xcor()
        new_x = self.xcor() + self.dx

        current_y = self.ycor()
        new_y = self.ycor() + self.dy

        right_side_ball = new_x + self.r
        left_side_ball = new_x - self.r

        up_side_ball = new_y + self.r
        down_side_ball = new_y - self.r

        self.goto(new_x, new_y)

        if (right_side_ball > screen_width / 2 and self.dx > 0) or  \
           (left_side_ball < -screen_width / 2 and self.dx < 0):
            self.dx = -self.dx
        if (up_side_ball > screen_height / 2 and self.dy > 0) or  \
           (down_side_ball < -screen_height / 2 and self.dy < 0):
            self.dy = -self.dy

    def grow(self, size=1):
        self.r += size
        self.shapesize(self.r / 10)


    def __str__(self):
        return '[x={}, y={}, r={}, dx={}, dy={}]'.format(self.xcor(), self.ycor(), self.r, self.dx, self.dy)




