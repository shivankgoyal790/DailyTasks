#------------------------------------------------------------------------------
# method 1 voilating interface segregation
# class Shape():
#     def returnside(self):
#         pass
#     def area(self):
#         pass
# -----------------------------------------------------------------------------


# method 2
class ShapewithSide():
    def returnside(self):
        pass

class Shapearea():
    def area(self):
        pass
    
#---------------------------------------------------------------------------------
class Circle(Shapearea):
    
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*(self.radius)*(self.radius)


class Square(Shapearea,ShapewithSide):

    def __init__(self,side):
        self.side = side
    def returnside(self):
        return self.side
    def area(self):
        return (self.side)*(self.side)

class Triangle(Shapearea,ShapewithSide):
    def __init__(self,side):
        self.side = side
    def returnside(self):
        return self.side
    def area(self):
        return (3**0.5) / 4 * (self.side)*(self.side)

c = Circle(2)
s = Square(2)
t = Triangle(3)
print(c.area())
print(s.area())
print(t.area())