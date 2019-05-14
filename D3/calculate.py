import math

class Equation:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def get_pos(self):
        return self.x, self.y, self.z
    def set_pos(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Line(Equation):
    def __init__(self, a, b, c, x, y, z):
        super().__init__(x, y, z)
        self.a = a
        self.b = b
        self.c = c
    def get_direction(self):
        return self.a, self.b, self.c
    def get_pos0(self):
        return self.x, self.y, self.z
    def calculate(self, t):
        x = self.x + t * self.a
        y = self.y + t * self.b
        z = self.z + t * self.c
        return x, y, z



class Calculate:
    def dist(self, point1, point2):
        math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)
    def line(self, point1, point2):
        t = self.dist(point1, point2)

        a = (point2[0] - point1[0]) / t
        b = (point2[1] - point1[1]) / t
        c = (point2[2] - point1[2]) / t

        return point1, (a, b, c)
    def POI(self, ob1, ob2):
        #point of intersection between line and plane
        if (type(ob1) or type(ob2)) == 'Line' and (type(ob1) or type(ob2)) == 'Plane':
            plane = [ob1, ob2][[type(ob1), type(ob2)].index('Plane')]
            line  = [ob1, ob2][[type(ob1), type(ob2)].index('Line')]

