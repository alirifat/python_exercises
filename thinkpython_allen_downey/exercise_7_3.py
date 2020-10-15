def square_root(a):
    x = 5
    a = float(a)
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.0000001:
            break
        x = y
    return y

def test_square_root(a):
    from math import sqrt
    test = square_root(a)
    real = sqrt(a)
    l_format = '{:<13}'
    print(float(a),
          l_format.format(str(square_root(a))[:13]),
          l_format.format(str(sqrt(a))[:13]),
          l_format.format(str(abs(real - test))[:13]))

for i in range(1, 10):
    test_square_root(i)
