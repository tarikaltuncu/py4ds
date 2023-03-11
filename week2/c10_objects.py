"""This module teaches what a Python class is and how to use it."""
import argparse

class Point():
    """A class that represents a point in 2D space."""

    def __init__(self, ilk_duzlem, y):
        """Initialize the point with x and y coordinates."""
        self.x = ilk_duzlem
        self.y = y

    def move(self, dx, dy):
        """Move the point by dx and dy."""
        self.x += dx
        self.y += dy

    def distance(self, another_point):
        """Compute the distance between this point and another point."""
        dx = self.x - another_point.x
        dy = self.y - another_point.y
        return (dx**2 + dy**2)**0.5

    def __str__(self):
        """Return a string representation of the point."""
        return '(%g, %g)' % (self.x, self.y)

    def __repr__(self):
        """Return a string representation of the point."""
        return 'Point(%f, %f)' % (self.x, self.y)

    def __eq__(self, other):
        """Return True if other is a Point with the same coordinates."""
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """Return True if other is not a Point with the same coordinates."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Return True if self is less than other."""
        return self.x < other.x or self.x == other.x and self.y < other.y

    def __gt__(self, other):
        """Return True if self is greater than other."""
        return self.x > other.x or self.x == other.x and self.y > other.y

    def __le__(self, other):
        """Return True if self is less than or equal to other."""
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        """Return True if self is greater than or equal to other."""
        return self.__gt__(other) or self.__eq__(other)

    def __add__(self, other):
        """Return the sum of self and other."""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Return the difference of self and other."""
        return Point(self.x - other.x, self.y - other.y)

def main():
    parser = argparse.ArgumentParser(description='Enter two points.')
    parser.add_argument('x1', type=float, help='the x coordinate of the first point')
    parser.add_argument('y1', type=float, help='the y coordinate of the first point')
    parser.add_argument('x2', type=float, help='the x coordinate of the second point')
    parser.add_argument('y2', type=float, help='the y coordinate of the second point')
    args = parser.parse_args()
    p1 = Point(args.x1, args.y1)
    p2 = Point(args.x2, args.y2)
    print('p1 =', repr(p1))
    print('p2 =', repr(p2))
    print('p1 =', str(p1))
    print('p2 =', str(p2))
    print('p1 + p2 =', p1 + p2)
    print('p1 - p2 =', p1 - p2)
    print('p1 == p2 is', p1 == p2)
    print('p1 != p2 is', p1 != p2)
    print('p1 < p2 is', p1 < p2)
    print('p1 > p2 is', p1 > p2)
    print('p1 <= p2 is', p1 <= p2)
    print('p1 >= p2 is', p1 >= p2)
    print('distance(p1, p2) =', p1.distance(p2))
    p1.move(1, 1)
    print('p1 after moving is', p1)
    print('distance(p1, p2) after moving p1 is', p1.distance(p2))

# main()

if __name__ == "__main__":
    main()