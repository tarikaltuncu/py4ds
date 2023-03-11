from math import pi, sqrt

def circle_area(radius):
    return pi * radius ** 2

def circumference(radius):
    return 2 * pi * radius

def side_length_of_a_square(area):
    return sqrt(area)

def side_length_of_a_qube(volume):
    return volume ** (1/3)

def main():
    print(circle_area(5))
    print(circumference(5))
    print(side_length_of_a_square(25))
    print(side_length_of_a_qube(125))

if __name__ == "__main__":
    main()