# Chapter 8 Exercises

# Review Questions (True/False)
# 1. False. It can implement a definite loop but it is mostly used for indefinite loops.

# 2. True.

# 3. False. It can ask in each iteration but it can also be used until the user input the sentinel value.

# 4. False.

# 5. False.

# 6. False. It can be a pre-test and a post-test loop depending on the structure.

# 7. True.

# 8. True.

# 9. False. It is (not a) and (not b).

# 10. True.


# Multiple Choice
# 1. A (interactive loop)
# 2. C (sentinel loop)
# 3. D (post-test loop)
# 4. C (sentinel loop)
# 5. C (break)
# 6. C (not (a and b) == not(a) and not(b))
# 7. D (infinite)
# 8. B (TFT)
# 9. C (FTF)
# 10. A (short-circuit)


# Discussion
# 1. a) A definite loop runs until it repeats a certain number of time or it traverses a list of items. However, an
# indefinite loop runs until it meets a certain condition.
# 1. b) A for loop is used when there is a list of objects to traverse. It can also be used to repeat a block of code
# for a certain number of times. A while loop is used when there is a certain condition to met. It executes the loop
# until the condition is met.
# 1. c) An interactive loop takes input from the user in each iteration. The user decides to terminate the loop by
# entering a special value or doing a certain thing. The sentinel loop is a concept to execute an indefinite loop
# until a special value is given. It can be an interactive loop or a data processing loop.
# 1. d) A sentinel loop is defined in the previous option. A end-of-file loop is a special case of sentinel loop which
# runs the loop until the file ends and returns an empty string. The special value can be altered, as well.

# 2. a)
# P     Q     P and Q     not (P and Q)
# T     T        T              F
# T     F        F              T
# F     T        F              T
# F     F        F              T

# 2. b)
# P     Q     not P     (not P) and Q
# T     T       F             F
# T     F       F             F
# F     T       T             T
# F     F       T             F

# 2. c)
# P     Q     not P     not Q     (not P) or (not Q)
# T     T       F         F               F
# T     F       F         T               T
# F     T       T         F               T
# F     F       T         T               T

# 2. d)
# P     Q     R     (P and Q)     (P and Q) or R
# T     T     T         T                T
# T     T     F         T                T
# T     F     T         F                T
# T     F     F         F                F
# F     T     T         F                T
# F     T     F         F                F
# F     F     T         F                T
# F     F     F         F                F

# 2. e)
# P     Q     R     (P or Q)     (Q or R)     (P or R) and (Q or R)
# T     T     T        T            T                   T
# T     T     F        T            T                   T
# T     F     T        T            T                   T
# T     F     F        T            F                   F
# F     T     T        T            T                   T
# F     T     F        T            T                   T
# F     F     T        F            T                   F
# F     F     F        F            F                   F

# 3. a)
# input validation
n = -1
while n < 1:
    n = int(input('Please! Enter the n for the sum of first n counting numbers [1]: '))

print('The sum of first {} counting numbers is '.format(n), end='')

total = 0
while n > 0:
    total += n
    n -= 1
print('{}.'.format(total))

# 3. b)
# input validation
n = -1
while n < 1:
    n = int(input('Please! Enter the n for the sum of first n odd numbers: '))

print('The sum of first {} odd numbers is '.format(n), end='')
total = 0
while n > 0:
    total += 2 * n - 1
    n -= 1
print('{}.'.format(total))

# 3. c)
total = 0
while True:
    n = int(input('Please enter a number [999 to quit]: '))

    if n == 999:
        break

    total += n

print('The sum of all numbers is {}.'.format(total))

# 3. d)
n = int(input('Please! Enter an integer: '))

print('The number of times {} can be divided by 2 without reaching to 1 is '.format(n), end='')
count = 0
while n > 1:
    n = n // 2
    count += 1

print('{}.'.format(count))


# # Programming Exercises
import math
from tkinter.filedialog import askopenfilename
from graphics import *
# 1.
def fibonacci():
    n = int(input('Please enter n for nth Fibonacci number: '))

    i = 1
    j = 1
    for idx in range(n - 2):
        j, i = i + j, j

    return 'The {}th Fibonacci number is {}.'.format(n, j)


print(fibonacci())


# 2.
def windchill_formula(v, t):
    return 35.74 + 0.6212 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)


def windchill_table():
    wind_speeds = range(5, 51, 5)
    temperatures = range(-20, 61, 10)

    print('Wind Speed', end='\t')
    print('{:^70}'.format('Temperature'))

    print('{:^10}'.format(''), end='\t')
    for temperature in temperatures:
        print('{:^6}'.format(temperature), end='\t')
    print()

    for v in wind_speeds:
        print('{:^10}'.format(v), end='\t')
        for t in temperatures:
            windchill = windchill_formula(v, t)
            print('{:^6.2f}'.format(windchill), end='\t')
        print()

    return


windchill_table()


# 3.
def how_many_years(apr):
    principal = 1
    target_amount = principal * 2

    count = 0
    while principal < target_amount:
        principal = (1 + apr) * principal
        count += 1

    return count


print(how_many_years(0.01))
print(how_many_years(1))


# 4.
def syracuse_sequence(n):
    sequence = [n]

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    return sequence


print(syracuse_sequence(5))
print(syracuse_sequence(13))
print(syracuse_sequence(37))


# 5.
def is_prime(n):
    limit = int(math.sqrt(n))

    for i in range(2, limit + 1):
        if n % i == 0:
            return False

    return True


print(is_prime(8))
print(is_prime(9))
print(is_prime(37))
print(is_prime(97))


# 6.
def find_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)

    return primes


print(find_primes(101))


# 7.
def find_goldbach():
    n = -1
    while n % 2 != 0 or n < 1:
        n = int(input('Please! Enter an even positive number: '))

    sums = []
    for i in range(2, n - 1):
        x = n - i
        if is_prime(i) and is_prime(x):
            sums.extend([(i, x)])

    return sums


print(find_goldbach())


# 8.
def find_gcd(m, n):
    while m != 0:
        n, m = m, n % m

    return n


print(find_gcd(22, 121))

# 9.
def calculate_mpg():
    mileage = []
    gas = []

    initial_reading = float(input('Please! Enter the odometer reading: '))
    mileage.append(initial_reading)

    idx = 1
    while True:
        leg_mile_gas = input('Enter the current odometer reading and the amount of gas [Press <Enter> to quit]: ')

        if not leg_mile_gas:
            break

        mileage.append(float(leg_mile_gas.split()[0]))
        gas.append(float(leg_mile_gas.split()[1]))

        miles_per_gallon = (mileage[idx] - mileage[idx-1]) / gas[idx-1]
        print('Leg {0}: MPG: {1:.1f}'.format(idx, miles_per_gallon))

        idx += 1

    miles_per_gallon_total = (mileage[-1] - mileage[0]) / sum(gas)
    print('Total MPG: {:.1f}'.format(miles_per_gallon_total))


calculate_mpg()

# 10.
def calculate_mpg_file():
    filename = askopenfilename()
    fin = open(filename, 'r')

    mileage = [float(fin.readline())]
    gas = []

    idx = 1
    while True:
        leg_mile_gas = fin.readline()

        if not leg_mile_gas:
            break

        mileage.append(float(leg_mile_gas.split()[0]))
        gas.append(float(leg_mile_gas.split()[1]))

        miles_per_gallon = (mileage[idx] - mileage[idx-1]) / gas[idx-1]
        print('Leg {0}: MPG: {1:.1f}'.format(idx, miles_per_gallon))

        idx += 1

    miles_per_gallon_total = (mileage[-1] - mileage[0]) / sum(gas)
    print('Total MPG: {:.1f}'.format(miles_per_gallon_total))


calculate_mpg_file()

# 11.
def heating_and_cooling_degrees():
    heating_degrees = 0
    cooling_degrees = 0

    lower_limit = 60
    upper_limit = 80

    while True:
        daily_average_temp = input('Please! Enter the daily average temperature [Press <Enter> to quit]: ')

        if not daily_average_temp:
            break

        daily_average_temp = float(daily_average_temp)
        if daily_average_temp < lower_limit:
            cooling_degrees += (lower_limit - daily_average_temp)

        if daily_average_temp > upper_limit:
            heating_degrees += (daily_average_temp - upper_limit)

    print('The total heating degrees: {}'.format(heating_degrees))
    print('The total cooling degrees: {}'.format(cooling_degrees))


heating_and_cooling_degrees()

# 12.
def heating_and_cooling_degrees_file():
    filename = askopenfilename()
    fin = open(filename, 'r')

    heating_degrees = 0
    cooling_degrees = 0

    lower_limit = 60
    upper_limit = 80

    while True:
        daily_average_temp = fin.readline()

        if not daily_average_temp:
            break

        daily_average_temp = float(daily_average_temp)
        if daily_average_temp < lower_limit:
            cooling_degrees += (lower_limit - daily_average_temp)

        if daily_average_temp > upper_limit:
            heating_degrees += (daily_average_temp - upper_limit)

    print('The total heating degrees: {}'.format(heating_degrees))
    print('The total cooling degrees: {}'.format(cooling_degrees))


heating_and_cooling_degrees_file()

# 13.
def draw_background(win, p1, p2, color='gray'):
    # draw the background
    rec = Rectangle(p1, p2)
    rec.setFill(color)
    rec.draw(win)

    return rec


def draw_text(win, p, text):
    # draw text
    message = Text(p, text)
    message.setTextColor('white')
    message.draw(win)

    return message


def draw_point(win, p, r, color='black'):
    c = Circle(p, r)
    c.setFill(color)
    c.draw(win)

    return c


def calculate_slope_and_means(sum_xy, x_square_total, n, total_x, total_y):
    x_bar = total_x / n
    y_bar = total_y / n

    nominator = (sum_xy - n * x_bar * y_bar)
    denominator = (x_square_total - n * (x_bar ** 2))

    m = nominator / denominator

    return x_bar, y_bar, m


def regression_plot(width, height):
    win = GraphWin('Regression Plot', width, height)
    win.setCoords(-10, -10, 10, 10)

    welcome_rec = draw_background(win, Point(-6, -1), Point(6, 1))
    welcome_text = 'Please! Click on the graph to locate the data points.'
    welcome_message = draw_text(win, Point(0, 0), welcome_text)

    start_rec = draw_background(win, Point(-1, -2.5), Point(1, -1.5))
    start_text = 'Start'
    start_message = draw_text(win, Point(0, -2), start_text)

    while True:
        p = win.getMouse()
        x = p.getX()
        y = p.getY()

        if (-1 <= x <= 1) and (-2.5 <= y <= -1.5):
            welcome_rec.undraw()
            welcome_message.undraw()
            start_rec.undraw()
            start_message.undraw()
            break

    exit_rec = draw_background(win, Point(-10, -10), Point(-8, -9))
    exit_text = 'Done!'
    exit_message = draw_text(win, Point(-9, -9.5), exit_text)

    radius = 0.1
    n = 0
    total_x = 0
    total_y = 0
    x_square_total = 0
    sum_xy = 0
    while True:
        p = win.getMouse()
        x = p.getX()
        y = p.getY()

        if (-10 <= x <= -8) and (-10 <= y <= -9):
            exit_rec.undraw()
            exit_message.undraw()
            break

        c = draw_point(win, p, radius)

        total_x += x
        total_y += y
        x_square_total += (x ** 2)
        sum_xy += (x * y)
        n += 1

    x_bar, y_bar, m = calculate_slope_and_means(sum_xy, x_square_total, n, total_x, total_y)

    left_x = -10
    left_end_y = y_bar + m * (left_x - x_bar)

    right_x = 10
    right_end_y = y_bar + m * (right_x - x_bar)

    l = Line(Point(left_x, left_end_y), Point(right_x, right_end_y))
    l.setFill('red')
    l.draw(win)

    win.getMouse()


regression_plot(640, 480)

# 14.
def read_image():
    image_file = askopenfilename()
    image = Image(Point(0, 0), image_file)
    return image


def photoshop_grayscale():
    image = read_image()
    width = image.getWidth()
    height = image.getHeight()

    # draw canvas
    win = GraphWin('Convert Grayscale', width, height)
    win.setCoords(-10, -10, 10, 10)
    image.draw(win)

    win.getMouse()

    for i in range(width):
        for j in range(height):
            rgb_colors = image.getPixel(i, j)
            r, g, b = rgb_colors[0], rgb_colors[1], rgb_colors[2]
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            image.setPixel(i, j, color_rgb(brightness, brightness, brightness))

    win.getMouse()

    r = Rectangle(Point(-9, -2), Point(9, 2))
    r.setFill('gray')
    r.draw(win)

    message = Text(Point(-6.5, 0), 'Save as: ')
    message.setTextColor('white')
    message.draw(win)

    entry_box = Entry(Point(2, 0), 12)
    entry_box.setText('grayscale.png')
    entry_box.draw(win)

    r_ok = Rectangle(Point(6.5, -2), Point(8.5, 2))
    r_ok.draw(win)
    message_ok = Text(Point(7.5, 0), 'OK')
    message_ok.setTextColor('white')
    message_ok.draw(win)

    click = win.getMouse()
    x = click.getX()
    y = click.getY()

    if (6.5 <= x <= 8.5) & (-2 <= y <= 2):
        filename = entry_box.getText()

        for shape in [r, message, entry_box, r_ok, message_ok]:
            shape.undraw()

        image.save(filename)


photoshop_grayscale()

# 15.
def read_image():
    image_file = askopenfilename()
    image = Image(Point(0, 0), image_file)
    return image


def photoshop(grayscale=True, negative=False):
    image = read_image()
    width = image.getWidth()
    height = image.getHeight()

    # draw canvas
    win = GraphWin('Convert Grayscale', width, height)
    win.setCoords(-10, -10, 10, 10)
    image.draw(win)

    win.getMouse()

    for i in range(width):
        for j in range(height):
            rgb_colors = image.getPixel(i, j)
            r, g, b = rgb_colors[0], rgb_colors[1], rgb_colors[2]
            if grayscale:
                brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
                image.setPixel(i, j, color_rgb(brightness, brightness, brightness))
            if negative:
                image.setPixel(i, j, color_rgb(255 - r, 255 - g, 255 - b))

    win.getMouse()

    r = Rectangle(Point(-9, -2), Point(9, 2))
    r.setFill('gray')
    r.draw(win)

    message = Text(Point(-6.5, 0), 'Save as: ')
    message.setTextColor('white')
    message.draw(win)

    entry_box = Entry(Point(2, 0), 12)
    entry_box.setText('new_file.png')
    entry_box.draw(win)

    r_ok = Rectangle(Point(6.5, -2), Point(8.5, 2))
    r_ok.draw(win)
    message_ok = Text(Point(7.5, 0), 'OK')
    message_ok.setTextColor('white')
    message_ok.draw(win)

    click = win.getMouse()
    x = click.getX()
    y = click.getY()

    if (6.5 <= x <= 8.5) & (-2 <= y <= 2):
        filename = entry_box.getText()

        for shape in [r, message, entry_box, r_ok, message_ok]:
            shape.undraw()

        image.save(filename)


photoshop(grayscale=False, negative=True)

# 16.
def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")


def handleClick(pt, win):
    entry = Entry(pt, 10)
    entry.draw(win)

    while True:
        key = win.getKey()
        print(key)
        if key == "Return":
            entry.undraw()
            typed = entry.getText()
            Text(pt, typed).draw(win)
            break
        if key == 'Escape':
            entry.undraw()
            break

    win.checkMouse()


def main():
    win = GraphWin("Click and Type", 500, 500)

    while True:
        key = win.checkKey()
        if key == 'q':  # loop exit
            break

        if key:
            handleKey(key, win)

        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)

    win.close()


main()
