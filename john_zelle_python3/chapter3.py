# Chapter 3 Exercises

# Review Questions (True/False)
# 1. True

# 2. False. int data types are exact numbers; thus, if should use int data type whenever it is possible to use. Floating
# points data type are stored as an approximate. For this reason, it should be avoid if we interested in finding the
# exact result.

# 3. False. Operations like addition and subtraction are defined as built-in numeric operations.

# 4. True

# 5. False. The sqrt function calculates a square root of a number.

# 6. False. A floating-point data type uses a formulaic representation of real numbers as an approximation so as to
# support a trade-off between range and precision. Thus, they are not identical to the real numbers.

# 7. True

# 8. True

# 9. True

# 10. False. The first one produces int data type. The second one produces a float data type.


# Multiple Choice
# 1. C (rational)
# 2. D (sqrt())
# 3. D (an import statement)
# 4. B (24)
# 5. B (float)
# 6. C (32)
# 7. D (ints to floats)
# 8. D (abs)
# 9. A (accumulator)
# 10. D (uses more memory)


# Discussion
# 1. a) float type
result_a = 4.0 / 10.0 + 3.5 * 2
print(type(result_a))

# 1. b) float type
result_b = 10 % 4 + 6 / 2
print(type(result_b))

# 1. c) int type
result_c = abs(4 - 20 // 3) ** 3
print(type(result_c))

# 1. d) illegal - ValueError, the value within the sqrt cannot be negative
# import math
# result_d = math.sqrt(4.5 - 5.0) + 7 * 3

# 1. e) int type
result_e = 3 * 10 // 3 + 10 % 3
print(type(result_e))

# 1. f) int type
result_f = 3 ** 3
print(type(result_f))

# 2. a)
# (3 + 4) * 5

# 2. b)
# n * (n - 1) / 2

# 2. c)
# 4 * math.pi * (r ** 2)

# 2. d)
# math.sqrt(r * math.cos(a) ** 2 + r * math.sin(b) ** 2)

# 2. e)
# (y2 - y1) / (x2 - x1)

# 3. a)
# [0, 1, 2, 3, 4]

# 3. b)
# [3, 4, 5, 6, 7, 8, 9]

# 3. c)
# [4, 7, 10]

# 3. d)
# [15, 13, 11, 9, 7]

# 3. e)
# []

# 4. a)
for i in range(1, 11):
    print(i * i)

# 4. b)
for i in [1, 3, 5, 7, 9]:
    print(i, ":", i ** 3)
print(i)

# 4. c)
x = 2
y = 10
for j in range(0, y, x):
    print(j, end='')
    print(x + y)
print('done')

# 4. d)
ans = 0
for i in range(1, 11):
    ans = ans + i * i
    print(i)
print(ans)

# 5. It would replace the numbers on the left of the point with 0.
print(round(314.159265, -1))
print(round(123.45678, -2))

# 6. a) -3
print(-10 // 3)

# 6. b) -1
print(-10 % 3)

# 6. c) -3
print(10 // -3)

# 6. d) -1
print(10 % -3)

# 6. e) 3
print(-10 // -3)


# Programming Exercises
# 1.
def main():
    import math

    print('This program calculates the volume and the surface area')
    print('of a sphere from a given radius.')

    radius = float(input('Enter the radius: '))

    volume = (4 / 3) * math.pi * (radius ** 3)
    surface_area = 4 * math.pi * (radius ** 2)

    print('The volume and surface area of a sphere with a radius of')
    print('{} is {} and {}, respectively.'.format(radius, volume, surface_area))


main()

# 2.
def main():
    import math

    print('This program calculates the cost per square inch of a')
    print('pizza given the diameter and the price.')

    diameter = float(input('Enter the diameter: '))
    price = float(input('Enter the price: '))

    surface_area = 4 * math.pi * (diameter / 2) ** 2
    cost_per_square = price / surface_area

    print('The cost per square of a pizza with {} diameter and {}'.format(diameter, price))
    print('price is {}.'.format(cost_per_square))


main()

# 3.
def main():
    print('This program calculates the molecular weight of a')
    print('carbohydrate given the number of hydrogen, carbon')
    print('and oxygen atoms.')

    hydrogen = int(input('Enter the number of hydrogen atoms: '))
    carbon = int(input('Enter the number of carbon atoms: '))
    oxygen = int(input('Enter the number of oxygen atoms: '))

    molecular_weight = 1.00794 * hydrogen + 12.0107 * carbon + 15.9994 * oxygen

    print('The total molecular weight is {}'.format(molecular_weight))


main()

# 4.
def main():
    print('This program calculates the distance to a lightning strike')
    print('based on the time elapsed between the flash and the sound.')

    time_elapsed = float(input('Enter the time elapsed between the flash and the sound in seconds: '))

    distance_in_ft = time_elapsed * 1100
    distance_in_miles = distance_in_ft / 5280

    print('The distance (in miles) to the lightning strike is', distance_in_miles)


main()

# 5.
def main():
    print('This program calculates the cost of a coffee order.')

    amount_in_pounds = float(input('Enter the amount of coffee order (in pounds): '))

    cost_of_coffee_per_pound = 10.50
    cost_of_shipping_per_pound = 0.86
    cost_overhead = 1.50

    cost_of_coffee_and_shipment = amount_in_pounds * (cost_of_coffee_per_pound + cost_of_shipping_per_pound)
    total_cost_of_order = cost_of_coffee_and_shipment + cost_overhead

    print('The total cost of ordering {} pounds coffee is', total_cost_of_order)


main()

# 6.
def main():
    print('This program calculates the slope between two points.')

    x1, y1 = eval(input('Enter the coordinates of the first point i.e. (x_1, y_1): '))
    x2, y2 = eval(input('Enter the coordinates of the second point i.e. (x_2, y_2): '))

    slope = (y2 - y1) / (x2 - x1)

    print('The slope between the two points is', slope)


main()

# 7.
def main():
    import math

    print('This program calculates the distance between two points.')

    x1, y1 = eval(input('Enter the coordinates of the first point i.e. (x_1, y_1): '))
    x2, y2 = eval(input('Enter the coordinates of the second point i.e. (x_2, y_2): '))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print('The distance between the two points is', distance)


main()

# 8.
def main():
    print('This program calculates the Gregorian epact based on the provided 4-digit year.')

    year = int(input('Enter a 4-digit year (i.e. 2013): '))

    C = year // 100
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30

    print('The Gregorian epact for year {} is {}'.format(year, epact))


main()

# 9.
def main():
    import math

    print('This program calculates the area of a triangle based on the length of its sides.')

    side_1 = float(input('Enter the length of the first side: '))
    side_2 = float(input('Enter the length of the second side: '))
    side_3 = float(input('Enter the length of the third side: '))

    s = (side_1 + side_2 + side_3) / 2
    area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))

    print('The area of a triangle with sides {}, {}, and {} is {}'.format(side_1, side_2, side_3, area))


main()

# 10.
def main():
    import math

    print('This program calculates the length of a ladder based')
    print('on the height and its angle (in degrees) with the wall.')

    height = float(input('Enter the height to reach with a ladder: '))
    degree = float(input('Enter the angel with the wall (in degrees): '))
    radians = (math.pi * degree) / 180
    length_ladder = height / math.sin(radians)

    print('The length of the ladder with height of {} and angle of {} is {}'.format(height, degree, length_ladder))


main()

# 11.
def main():
    print('This program calculates the sum of first n natural numbers.')

    n = int(input('Enter the n value: '))
    sum_of_first_n_numbers = n * (n + 1) / 2

    print('The sum of first {} numbers is {}'.format(n, sum_of_first_n_numbers))


main()

# 12.
def main():
    print('This program calculates the sum of cubes of the first n natural numbers.')

    n = int(input('Enter the n value: '))
    sum_cube_of_first_n_numbers = (n / 2) * (1 + n)

    print('The sum of the cubes of the first {} natural numbers is {}.'.format(n, sum_cube_of_first_n_numbers))


main()

# 13.
def main():
    print('This program sums a series of number entered by the user.')

    n = int(input('Enter the number of numbers to sum (n): '))

    total = 0
    for i in range(n):
        j = int(input('Enter an integer number: '))
        total = total + j

    print('The sum of all numbers is', sum)


main()

# 14.
def main():
    print('This program calculates the average of number entered by the user.')

    n = int(input('Enter the number of numbers to calculate the average (n): '))

    total = 0
    for i in range(n):
        j = int(input('Enter an integer number: '))
        total = total + j

    average = total / n

    print('The average of the numbers is', average)


main()

# 15.
def main():
    import math

    print('Approximates pi by using a series and returns the approximation error.')

    n = int(input('Enter the length of the series (n i.e. 5): '))

    total = 0
    for i in range(n):
        total = 4 * ((1 / (n + 1)) - (1 / (n + 3)))

    pi = math.pi
    error = pi - total

    print('The approximation error is', errro)


main()

# 16.
def main():
    print('This program calculates the nth Fibonacci term.')

    n = int(input('Enter the number of term (n): '))

    i = 0
    j = 1
    for idx in range(n - 1): # since the above definition is the first term of the series
        j, i = i + j, j

    print('The {}th term of Fibonacci series is {}.'.format(n, j))


main()

# 17.
def main():
    print("This program finds the square root of a given number by applying Newton's method.")

    x = int(input('Enter the number that you want to find the square root: '))
    n = int(input('How many times you want to improve the result: '))

    guess = x / 2
    for i in range(n):
        guess = (guess + (x / guess)) / 2

    print('The square root of {} is {}'.format(x, guess))


main()