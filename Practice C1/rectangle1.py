class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

class Square:
    def __init__(self,c):
        self.c = c
    def get_area_square(self):
        return self.c ** 2

class Circle:
    def __init__(self, a):
        self.a = a
    def get_area_circle(self):
        return (self.a ** 2) * 3.14