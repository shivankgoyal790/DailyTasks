# class Line():

#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2

#     def distance(self):
#         x1 = self.coor1[0]
#         y1 = self.coor1[1]
#         x2 = self.coor2[0]
#         y2 = self.coor2[1]
#         return  ((x1-x2) ** 2 + (y2-y1) ** 2) ** 0.5


# obj1 = Line((3,2),(8,10))
# print(obj1.distance())


class Rectangle():

    def __init__(self, x, y):
        self.l = x
        self.b = y

    def area(self):
        return self.l * self.b

    def print(self):
        print("hi")


class Square(Rectangle):

    def __init__(self, x, y):
        Rectangle.__init__(self, x, y)

    def print(self):
        print("bye")


r = Rectangle(3, 4)
s = Square(1, 2)
s = r

print(r.area())
