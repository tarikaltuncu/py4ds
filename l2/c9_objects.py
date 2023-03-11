"""This module teaches what a Python class is and how to use it."""
import argparse

class Point():
    """A class that represents a point in 2D space."""

    # def __init__(self):
    #     pass

    def __init__(self, x, y):
        """Initialize the point with x and y coordinates."""
        self.x = x
        self.y = y

    def yazdir(self):
        """Return a string representation of the point."""
        return 'Nokta(%d, %d)' % (self.x, self.y)

    def __str__(self):
        """Return a string representation of the point."""
        return 'Point(%d, %d)' % (self.x, self.y)

def main():
    parser = argparse.ArgumentParser(description='Enter two points.')
    parser.add_argument('x1', type=float, help='the x coordinate of the first point')
    parser.add_argument('y1', type=float, help='the y coordinate of the first point')
    args = parser.parse_args()
    p = Point(x = args.x1, y = args.y1)
    print(p.yazdir())
    print(p)

if __name__ == "__main__":
    main()