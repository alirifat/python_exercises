def do_n(f, n):
    if n <= 0:
        return
    f()
    do_n(f, n-1)

def print_test():
    print('test')

do_n(print_test, 3)
