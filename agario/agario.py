import turtle
import time
import random
from ball import Ball
import math

screen = turtle.Screen()
bg = "agar2.gif"
screen.addshape(bg)
t = turtle.clone()
t.shape(bg)

def get_random_ball_attributes():
    X = random.randint(-SCREEN_WIDTH // 2 + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH // 2 - MAXIMUM_BALL_RADIUS)
    Y = random.randint(-SCREEN_HEIGHT // 2 + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT // 2 - MAXIMUM_BALL_RADIUS)
    X_axis_speed = 0
    Y_axis_speed = 0
    while X_axis_speed == 0 or Y_axis_speed == 0:
        X_axis_speed = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
        Y_axis_speed = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    Radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
    Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    return X, Y, X_axis_speed, Y_axis_speed, Radius, Color


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
            if collide(ball_a, ball_b):
                print("Yes")
                rad_a = ball_a.r
                rad_b = ball_b.r
                if rad_a > rad_b:
                    ball_a.grow()
                    ball_b.hideturtle()
                    col = True
                    while col:
                        X, Y, X_axis_speed, Y_axis_speed, Radius, Color = get_random_ball_attributes()
                        # ball_b.__init__(X, Y, X_axis_speed, Y_axis_speed, Radius, Color)
                        ball_b.hideturtle()
                        ball_b.goto(X, Y)
                        ball_b.r = Radius

                        col = False
                        for ball in BALLS:
                            if collide(ball_b, ball):
                                col = True
                            if collide(ball_b, MY_BALL):
                                col = True
                                break

                        if not col:
                            ball_b.dx = X_axis_speed
                            ball_b.dy = Y_axis_speed
                            ball_b.shapesize(Radius / 10)
                            ball_b.color(Color)
                            print(ball_b)
                            ball_b.showturtle()

                elif rad_b > rad_a:
                    ball_b.grow()
                    ball_a.hideturtle()
                    col = True
                    while col:
                        X, Y, X_axis_speed, Y_axis_speed, Radius, Color = get_random_ball_attributes()
                        # ball_a.__init__(X, Y, X_axis_speed, Y_axis_speed, Radius, Color)
                        ball_a.hideturtle()
                        ball_a.goto(X, Y)
                        ball_a.r = Radius
                        col = False
                        for ball in BALLS:
                            if collide(ball_a, ball):
                                col = True
                            if collide(ball_a, MY_BALL):
                                col = True
                                break
                        if not col:
                            ball_a.dx = X_axis_speed
                            ball_a.dy = Y_axis_speed
                            ball_a.shapesize(Radius / 10)
                            ball_a.color(Color)
                            print(ball_a)
                            ball_a.showturtle()
                            break
check_run = True

def check_myball_collision():
    global check_run
    for ball in BALLS:
        if collide(ball, MY_BALL) == True:
            print("My_Yes")
            r_b = ball.r
            r_my_b = MY_BALL.r



            if r_b > r_my_b:
                ball.grow()
                check_run = False

            elif r_my_b > r_b:
                MY_BALL.grow()



                col = True
                while col:
                    X, Y, X_axis_speed, Y_axis_speed, Radius, Color = get_random_ball_attributes()
                    ball.hideturtle()
                    ball.goto(X, Y)
                    ball.r = Radius

                    col = False
                    for ball2 in BALLS:
                        if collide(ball, ball2):
                            col = True
                        elif collide(ball, MY_BALL):
                            col = True
                            break

                    if not col:
                        ball.dx = X_axis_speed
                        ball.dy = Y_axis_speed
                        ball.shapesize(Radius / 10)
                        ball.color(Color)
                        print(ball)
                        ball.showturtle()


mouse_x = 0
mouse_y = 0
def movearound(event):
    global mouse_x
    global mouse_y
    mouse_x = event.x - SCREEN_WIDTH // 2
    mouse_y = event.y * -1 + SCREEN_HEIGHT // 2
    d = math.sqrt(pow(mouse_x - MY_BALL.xcor(), 2) + pow(mouse_y - MY_BALL.ycor(), 2))
    d_my = math.sqrt(pow(MY_BALL.dx, 2) + pow(MY_BALL.dy, 2))
    MY_BALL.dx = (mouse_x - MY_BALL.xcor()) / (d / d_my)
    MY_BALL.dy = (mouse_y - MY_BALL.ycor()) / (d / d_my)

turtle.tracer(0)
turtle.hideturtle()
turtle.colormode(255)

SLEEP = 0.0077
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width())
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height())
print('Screen width: {}, height: {}'.format(SCREEN_WIDTH, SCREEN_HEIGHT))

MY_BALL = Ball(0, 0, 3, 3, 50, "green")

MY_BALL.showturtle()


NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 80
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []



for i in range(NUMBER_OF_BALLS):
    c = True
    print(i)
    x, y, dx, dy, radius, color = get_random_ball_attributes()
    # while x + 100 <= MY_BALL.xcor() or x - 100 <= MY_BALL.xcor() or y + 100 <= MY_BALL.ycor() or y - 100 <= MY_BALL.ycor():
    while c:
        x, y, dx, dy, radius, color = get_random_ball_attributes()
        ball = Ball(x, y, dx, dy, radius, color)
        d = math.sqrt(pow(x - MY_BALL.xcor(), 2) + pow(y - MY_BALL.ycor(), 2) + 10)
        sum_r = radius + MY_BALL.r
        if d >= sum_r:
            c = False
    BALLS.append(ball)

for ball in BALLS:
    ball.showturtle()

turtle.Screen().getcanvas().bind('<Motion>', movearound)

time.sleep(2)

RUNNING = True



place = 6
old_p = 6

mass = MY_BALL.r
old_m = mass

turtle.hideturtle()
turtle.penup()

mass_t = turtle.clone()
mass_t.hideturtle()
mass_t.penup()

turtle.goto(-SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 50)
mass_t.goto(-SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 - 50)
turtle.write("Place: " + str(place))
mass_t.write("Mass: " + str(mass))


while RUNNING:
    old_m = mass
    mass = MY_BALL.r

    print(RUNNING)
    old_s_w = SCREEN_WIDTH
    SCREEN_WIDTH = int(turtle.getcanvas().winfo_width())
    if old_s_w != SCREEN_WIDTH:
        turtle.clear()
        turtle.write("Place: " + str(place))
        mass_t.clear()
        mass_t.write("Mass: " + str(mass))
    old_s_h = SCREEN_HEIGHT
    SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height())
    if old_s_w != SCREEN_HEIGHT:
        turtle.clear()
        turtle.write("Place: " + str(place))
        mass_t.clear()
        mass_t.write("Mass: " + str(mass))

    turtle.goto(-SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 50)
    mass_t.goto(-SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 - 50)
    check_myball_collision()
    check_all_balls_collision()
    RUNNING = check_run
    move_all_balls()
    MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.update()
    time.sleep(0.05)

    old_p = place
    place = 6
    for ball in BALLS:
        if MY_BALL.r > ball.r:
            place = place - 1

    if old_p != place:
        turtle.clear()
        turtle.write("Place: " + str(place))

    if old_m != mass:
        mass_t.clear()
        mass_t.write("Mass: " + str(mass))














