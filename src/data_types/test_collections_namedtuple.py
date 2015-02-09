from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'], verbose=True)

print Point
p = Point(11, y=22)

print p[0] + p[1]
x, y = p
print x, y

print p.x + p.y


print 'Unpacking Aggument Lists'

d = {'x': 11, 'y': 22}
print Point(**d)


'''change functionality with a subclass'''
class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)


for p in Point(3, 4), Point(14, 5/7.):
    print p


print Point._fields + ('z', )