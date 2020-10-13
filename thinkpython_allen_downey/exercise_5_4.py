def is_triangle(a, b, c):
    if a > b+c:
        print('No')
    elif b > a+c:
        print('No')
    elif c > a+b:
        print('No')
    else:
        print('Yes')

def get_input():
    a = int(input('Please enter a value for the first side of the triangle:'))
    b = int(input('Please enter a value for the second side of the triangle:'))
    c = int(input('Please enter a value for the third side of the triangle:'))
    is_triangle(a, b, c)

get_input()
