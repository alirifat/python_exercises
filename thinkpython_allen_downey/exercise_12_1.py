def sumall(*args):
    count = 0
    for arg in args:
        count += arg
    return count

print(sumall(1,2,3,4,4,5,6,7))
print(sumall(1,2,34))
numbers = 1,2,3,4,5,6,6,7,8,9
print(sumall(*numbers))
