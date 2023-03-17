from c10_objects import Point

with open('points.txt', 'r') as f:
    points = f.read().split(';')
    print(points)

    for point in points:
        coordinates = point.strip('()').split(', ')
        print(coordinates)
        p = Point(int(coordinates[0]), int(coordinates[1]))
        p.move(1,1)
        print(p)