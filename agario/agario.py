import turtle
import time
import random
from ball import Ball
import math


turtle.tracer()
turtle.hideturtle()
turtle.colormode(255)

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width() / 2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height() / 2)

MY_BALL = Ball(0, 0, 0, 0, 10, "green")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range(NUMBER_OF_BALLS):
    print(i)
    print(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
    x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
    y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
    dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
    dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #color = (random.random(), random.random(), random.random())
    ball = Ball(x, y, dx, dy, radius, color)
    BALLS.append(ball)

def move_all_balls():
    for ball in BALLS:
        ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)


def collide(ball_a, ball_b):
    if ball_a == ball_b:
        return False
    d = math.sqrt(pow(ball_a.xcor() - ball_b.xcor(), 2) + pow(ball_a.ycor() - ball_b.ycor(), 2) + 10)
    sum_r = ball_a.r + ball_b.r
    if d <= sum_r:
        return True
    else:
        return False

def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a, ball_b) == True:
                print("Yes")
                rad_a = ball_a.r
                rad_b = ball_b.r
                X = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
                Y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
                X_axis_speed = 0
                Y_axis_speed = 0
                while X_axis_speed == 0 or Y_axis_speed == 0:
                    X_axis_speed = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                    Y_axis_speed = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                Radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                #if rad_a > rad_b:
                   # ball_a.r = rad_a + rad_b
                   # ball_b = Ball(X, Y, X_axis_speed, Y_axis_speed, Radius, Color)
                #if rad_b > rad_a:
                   # ball_b.r = rad_a + rad_b
                   # ball_a = Ball(X, Y, X_axis_speed, Y_axis_speed, Radius, Color)
                if rad_a > rad_b:
                    ball_a.r = rad_a + 1

                    ball_b.x = X
                    ball_b.y = Y
                    ball_b.dx = X_axis_speed
                    ball_b.dy = Y_axis_speed
                    ball_b.r = Radius
                    ball_b.color = Color

                if rad_a > rad_b:
                    ball_b.r = rad_a + 1

                    ball_a.x = X
                    ball_a.y = Y
                    ball_a.dx = X_axis_speed
                    ball_a.dy = Y_axis_speed
                    ball_a.r = Radius
                    ball_a.color = Color
                    ball_a.shapesize(Radius/10)
                    #ball_a.color(Color)
                    ball_a.goto(X, Y)
                    
                    

def check_myball_collision():
    for ball in BALLS:
        if collide(ball, MY_BALL) == True:
            print("My_Yes")
            r_b = ball.r
            r_my_b = MY_BALL.r 
            X = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
            Y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
            X_axis_speed = 0
            Y_axis_speed = 0
            while X_axis_speed == 0 or Y_axis_speed == 0:
                X_axis_speed = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                Y_axis_speed = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
            Radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
            Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            if r_b > r_my_b:
                ball.r = r_b + 1

                MY_BALL.x = X
                MY_BALL.y = Y
                MY_BALL.dx = X_axis_speed
                MY_BALL.dy = Y_axis_speed
                MY_BALL.r = Radius
                MY_BALL.color = Color

            if r_my_b > r_b:
                MY_BALL.r = r_my_b + 1

                ball.x = X
                ball.y = Y
                ball.dx = X_axis_speed
                ball.dy = Y_axis_speed
                ball.r = Radius
                ball.color = Color
                ball.shapesize(Radius/10)
                #ball.color(Color)
                ball.goto(X, Y)
        
        
    



check_all_balls_collision()
move_all_balls()





