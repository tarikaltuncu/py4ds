from c10_objects import Point

p1 = Point(3, 4)
p2 = Point(5, 12)

with open('points.txt', 'w') as f:
    f.write(str(p1) + ';' + str(p2))