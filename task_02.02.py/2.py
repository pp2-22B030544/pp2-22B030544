import math
class Point(object) :
    def __init__(self, x ,y):
        self.x =x
        self.y =y
    def get_x(self):
        return self.x
    def get_y(self) :
        return self.y
    def shift(self, dx, dy):
        self.x+=dx 
        self.y += dy
    def distance(self, other) :
        dx = other.x -self.x
        dy = other.y - self.y
        return math.sqrt(dx*dx + dy *dy)    