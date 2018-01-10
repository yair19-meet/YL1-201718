import turtle
import time
import random
from ball import Ball


turtle.tracer()
turtle.hideturtle()
turtle.colormode(255)

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT =  turtle.getcanvas().winfo_height()/2

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
    x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
    y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
    dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
    dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    ball = Ball(x, y, dx, dy, radius, color)
    BALLS.append(ball)

def move_all_balls():
    for index in range(len(BALLS)):
        BALLS(index).move(400, 400)
    

