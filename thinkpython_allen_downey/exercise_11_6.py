def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


known = {0:0, 1:1}

def fibonacci_modified(n):
    if n in known:
        return known[n]
    res = fibonacci_modified(n-1) + fibonacci_modified(n-2)
    known[n] = res
    return res

def get_time(f, i):
    import time
    start = time.time()
    value = f(i)
    return time.time() - start, value

print(' ', 'original', 'modified')
for i in [5, 10, 15, 20, 25, 30]:
    org_time, org_value = get_time(fibonacci, i)
    mod_time, mod_value = get_time(fibonacci_modified, i)
    print(i, org_value, mod_value)
    print(' ', org_time, mod_time)
