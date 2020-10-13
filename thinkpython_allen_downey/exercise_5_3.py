def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work")

def get_input():
    a = int(input('Please enter a value for a:'))
    b = int(input('Please enter a value for b:'))
    c = int(input('Please enter a value for c:'))
    n = int(input('Please enter a value for n:'))
    check_fermat(a, b, c, n)

get_input()
