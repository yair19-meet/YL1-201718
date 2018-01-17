import turtle
import time
import random
from ball import Ball
import random
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
    ball = Ball(x, y, dx, dy, radius, color)
    BALLS.append(ball)

def move_all_balls():
    for ball in BALLS:
        ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)
move_all_balls()

def collide(ball_a, ball_b):
    if ball_a == ball_b:
        return False
    d = sqrt(pow(ball_a.xcor() - ball_b.xcor()) + pow(ball_a.ycor() - ball_b.ycor())) + 10
    sum_r = ball_a.r + ball_b.r
    if d <= sum_r:
        return True
    else:
        return False

def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a, ball_b) == True:
                rad_a = ball_a.r
                rad_b = ball_b.r
                X = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
                Y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
                X_axis_speed = 0
                Y_axis_speed = 0
                while x_axis_speed == 0 or y_axis_speed == 0:
                    X_axis_speed = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                    Y_axis_speed = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                Radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if rad_a > rad_b:
                    ball_a.r = rad_a + rad_b
                    ball_b = Ball(X, Y, X_axis_speed, Y_axis_speed, Radius, Color)
                if rad_b > rad_a:
                    ball_b.r = rad_a + rad_b
                    ball_a = Ball(X, Y, X_axis_speed, Y_axis_speed, Radius, Color)
check_all_balls_collision()





