import math

class Shape:
    def what_am_i(self):
        print("I am a Shape.")

class Rectangle(Shape):
    def __init__(self, l):
        self.len = l
        
    def calculate_perimeter(self):
        return 4 * self.len


class Square(Shape):
    def __init__(self,l):
        self.len = l
        
    def calculate_perimeter(self):
        return math.pi * self.len * 2
    
    def change_size(self,cl):
        self.len = cl

class Horse:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


jack = Person("Taro")
makiba_oh = Horse("Makiba oh", "uma", jack)
print(makiba_oh.owner.name)


#rtg = Rectangle(3)
#print(rtg.calculate_perimeter())
#print(rtg.what_am_i())

#sqr = Square(5)
#print(sqr.calculate_perimeter())
#print(sqr.what_am_i())

#sqr.change_size(6)
#print(sqr.calculate_perimeter())


