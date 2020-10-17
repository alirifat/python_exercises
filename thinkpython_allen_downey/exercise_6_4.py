#
#             |-----------------------------------|
# <module>    | x ---> 1                          |
#             | y ---> x + 1                      |
#             |-----------------------------------|
#
#             |-----------------------------------|
#             | x      ---> 1                     |
# c           | y      ---> y + 3       ---> 5    |
#             | z      ---> x + y       ---> 3    |
#             | total  ---> x + y + z   ---> 9    |
#             | square ---> b(total)**2 ---> 8100 |
#             |-----------------------------------|
#
#             |-----------------------------------|
# b           | z    ---> x + y  ---> 3           |
#             | prod ---> a(z,z) ---> 12          |
#             |-----------------------------------|
#
#             |-----------------------------------|
# a           | x ---> x+1 ---> z+1 ---> 4        |
#             | y ---> z   ---> 3                 |
#             |-----------------------------------|

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))

# the program prints the local variable total which is x + y + z (the parameters
# of the function c) and the result of the function a which takes total as
# parameters for both of its arguments x and y. 
# the program also prints the final result in the function c.
