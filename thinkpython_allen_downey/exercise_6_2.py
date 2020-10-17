# def hypotenuse(x, y):
#     return 0.0
#
# print(hypotenuse(3, 4))
#
# def hypotenuse(x, y):
#     square_x = x**2
#     square_y = y**2
#     print('square_x is', square_x)
#     print('square_y is', square_y)
#     return 0.0
#
# print(hypotenuse(3, 4))
#
# def hypotenuse(x, y):
#     from math import sqrt
#     square_x = x**2
#     square_y = y**2
#     h_square = square_x + square_y
#     print('hypotenuse square is', h_square)
#     result = sqrt(h_square)
#     return result
#
# print(hypotenuse(3, 4))

def hypotenuse(x, y):
    from math import sqrt
    return sqrt(x**2 + y**2)

print(hypotenuse(3, 4))
