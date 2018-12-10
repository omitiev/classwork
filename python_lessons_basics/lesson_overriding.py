class Shape(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# sh1 = Shape(1,2)
# sh2 = Shape(1,3)
# print(sh1 == sh2)

class Point(Shape):

    def __init__(self, x, y):
        super().__init__(x, y)


class Circle(Shape):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def __doc__(self):
        return "This class represents Circle entity"

    def __eq__(self, other):
         return super().__eq__(other) and self.r == other.r

    def __str__(self):
        return "Circle %d, %d with radius %d" % (self.x, self.y, self.r)

p = Point(1,1)
c1 = Circle(1,2,3)
c2 = Circle(1,2,3)
print(c1 == c2)
print(c1)



v = 42
print(v.__add__(2))
print(v.__bool__())
print(v.__le__(12))
print(v.__mul__(10))


s = "abc"
print(s.__getitem__(2))

l = list(s)
print(l.__getitem__(2))
l.__setitem__(2, "x")
print(l.__str__())

class FancyList(list):

    def __str__(self):
        result = "[\n"
        result += ",\n\t".join(self)
        result += "]"
        return result


lst2 = FancyList()
lst2.append("a")
lst2.append("b")
lst2.append("c")
print(lst2)
# print(v.__bool__())
# print(v.__le__(12))
# print(v.__mul__(10))
