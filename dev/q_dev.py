class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    def norm(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, delta):
        self.x += delta.x
        self.y += delta.y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Rectangle:

    def __init__(self, leftbottom_corner, width, height):
        self.leftbottom_corner = leftbottom_corner
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @property
    def height(self):
        return self.height

    @property
    def leftbottom_corner(self):
        return self.leftbottom_corner

    @property
    def lefttop_corner(self):
        lefttop = self.leftbottom_corner
        lefttop.move(Point(0,self.height))
        return lefttop

    @property
    def rightbottom_corner(self):
        rightbottom = self.leftbottom_corner
        rightbottom.move(Point(self.width,0))
        return rightbottom

    @property
    def righttop_corner(self):
        righttop = self.leftbottom_corner
        righttop.move(Point(self.width,self.height))
        return righttop

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return self.width * 2 + self.height * 2

    def resize(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight

    def move(self, delta):
        self.leftbottom_corner.x += delta.x
        self.leftbottom_corner.y += delta.y

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.leftbottom_corner, self.width, self.height)

r1 = Rectangle(Point(0, 0), 100, 200)
r2 = Rectangle(Point(100, 80), 5, 10)
print("retângulo 1: ", r1)
print("retângulo 2: ", r2)