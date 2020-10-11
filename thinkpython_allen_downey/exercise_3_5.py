def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def pattern1():
    print('+----', end='')

def pattern2():
    print('|    ', end='')

def plus():
    print('+')

def vertical():
    print('|')

def row1():
    do_four(pattern1)
    plus()

def row2():
    do_four(pattern2)
    vertical()

def block():
    row1()
    do_four(row2)

def grid():
    do_four(block)
    row1()

grid()
