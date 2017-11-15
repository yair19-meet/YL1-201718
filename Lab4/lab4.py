class Animal(object):
    def __init__(self, sound, name, age, favorite_color):
        self.sound = sound
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
    def eat(self, food):
            print("Yummy!! " + self.name + " is eating " + food)
    def make_sound(self, signature):
        print((signature + " ")*3)
    def sound(self, sound, times):
        print((sound + " ") * times)
    def description(self):
            print(self.name + " is " + str(self.age) + " years old and loves the color " + self.favorite_color)
lion = Animal("RRRR","lion", 12, "yellow.")
lion.eat("this.")
lion.description()
lion.make_sound("LO")
lion.sound("fe", 4)
