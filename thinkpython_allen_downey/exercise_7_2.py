def square_root(a, epsilon):
    x = 5
    a = float(a)
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return y

print(square_root(a=64, epsilon=0.0001))
