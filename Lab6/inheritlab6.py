from turtle import *
from random import randrange
import time

colormode(255)




class Rectangle(Turtle):
    def __init__(self, width, hieght):
        Turtle.__init__(self)
        self.width = width
        self.hieght = hieght
        self.setheading(90)
        register_shape("rec", ((0, 0), (width, 0), (width, hieght), (0, hieght), (0, 0)))
        self.shape("rec")

#rec1 = Rectangle(100, 250)

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    def random_color2(self):
        for i in range(10):
            r = randrange(256)
            g = randrange(256)
            b = randrange(256)
            self.color(r, g, b)
            time.sleep(1)









    def random_color(self):
        r = randrange(256)
        g = randrange(256)
        b = randrange(256)
        self.color(r, g, b)


#square1 = Square(15)
#square1.random_color2()
#square1.size()

class Hexagon(Turtle):
    def __init__(self, size):
        Turtle.__init__(self)
        self.shapesize(size)
        begin_poly()
        for i in range(6):
            fd(20)
            right(60)
        end_poly()
        g = get_poly()
        register_shape("Hexagon", g)
        self.shape("Hexagon")

#hex1 = Hexagon(5)

class Polygon(Turtle):
    def __init__(self, line):
        Turtle.__init__(self)
        self.line = line
        self.shapesize(10)
        self.setheading(90)
        begin_poly()
        for i in range(line):
            fd(10)
            right(360/line)
        end_poly()
        shape = get_poly()
        register_shape("Poly", shape)
        self.shape("Poly")



Polygon(6)








mainloop()










