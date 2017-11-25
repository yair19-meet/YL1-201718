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

    def make_sound2(self, sound, times):
        print((sound + " ") * times)

    def description(self):
            print(self.name + " is " + str(self.age) + " years old and loves the color " + self.favorite_color)


lion = Animal("RRRR","lion", 12, "yellow.")
lion.eat("this.")
lion.description()
lion.make_sound("LO")
lion.make_sound2("fe", 4)


class Person(object):
    def __init__(self, name, age, city, gender):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender

    def eat_break(self, a):
        print(self.name + " ate his favorite breakfast: " + a)

roy = Person("Roy", 17, "New York", "Male")
roy.eat_break("omlet")
