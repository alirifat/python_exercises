def is_power(a, b):
    if a == b:
        return True
    else:
        if a % b == 0:
            return is_power(a/b, b)
        else:
            return False

print(is_power(100, 10))
