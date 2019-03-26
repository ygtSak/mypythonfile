class Shape:
    def __init__(self, l, w):
        print("1")
        self.width = w
        self.len = l

    def print_size(self):
        print("2")
        print("{} by {}".format(self.width, self.len))


class Square(Shape):
    def area(self):
        print("3")
        return self.width * self.len

    def print_size(self):
        print("4")
        print("I am {} by {}.".format(self.width,self.len))




a_square = Square(20,20)
print(a_square.print_size())
print(a_square.area())
