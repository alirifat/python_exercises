def distance_between_points(p1, p2):
    from math import sqrt
    distance_x = p1[0] - p2[0]
    distance_y = p1[1] - p2[1]
    return sqrt(distance_x**2 + distance_y**2)

print(distance_between_points((1,2), (3,4)))
