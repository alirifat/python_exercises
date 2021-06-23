# Chapter 6 Exercises

# Review Questions (True/False)
# 1. False.

# 2. False.

# 3. True.

# 4. True.

# 5. False.

# 6. False.

# 7. False.

# 8. True.

# 9. True.

# 10. False.


# Multiple Choice
# 1. B (caller)
# 2. A (def)
# 3. A (return)
# 4. B (position)
# 5. D (Control returns to the point just before the function was called.)
# 6. A (by value)
# 7. D (to demonstrate intellectual superiority)
# 8. A (an expression)
# 9. D (None)
# 10. A (mutable)


# Discussion
# 1. There are two motivations for defining functions: less and modular code. Functions help us to code less by
# preventing duplicate blocks of code. It also helps to maintain the code easily. On the other hand, functions can
# make the code modular by assigning each task to a single function. Thus, we can write a cleaner code.

# 2. It is true in general sense. However, we have to define the functions before calling them. Also, the code will
# be suspended and the controller will move to the line where the function defined when a function is called. Thus,
# it moves back and forward as we call functions.

# 3. a) Parameters helps to move information to function. They act as variables that are specific to a function.
# 3. b) An actual parameter is the value that will be passed to the function. The formal parameters are like the
# variables and the actual parameters are the information that are contained in those variables.
# 3. c) They are similar to ordinary variables in terms of carrying information. However, parameters are only defined
# within the borders of the function. In other words, they are local. Thus, they cannot be accessed outside of the
# function.

# 4. a) With the help of parameters.
# 4. b) With return keyword.

# 5. a) It takes a number and return its cube.
# 5. b)
# def cube(x):
#     answer = x * x * x
#     return answer
#
#
# print(cube(3))
# 5. c) It is due to the scope of the variables. The variable `answer` is defined outside of the function, which is
# different than the `answer` variable within the function. They do not have any connection. The cube function has
# an input of 3.


# Programming Exercises
import math
from graphics import *
from tkinter.filedialog import askopenfile

# 1.
def reprise():
    print('Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!')


def main(animal, sound):
    line1 = 'And on that farm he had a {}, Ee-igh, Ee-igh, Oh!'.format(animal)
    line2 = 'With a {0}, {0} here and a {0}, {0} there.'.format(sound)
    line3 = 'Here a {0}, there a {0}, everywhere a {0}, {0}.'.format(sound)

    print('{}\n{}\n{}'.format(line1, line2, line3))


def song(animal, sound):
    reprise()
    main(animal, sound)
    reprise()


song('cow', 'moo')
print()
song('chicks', 'cluck-cluck')
print()
song('duck', 'quack')
print()
song('sheep', 'baaa')
print()
song('turkey', 'gobble')

# 2.
def boom():
    print('Boom! Boom! Boom!')


def ants_marching(count):
    hurrah = 'hurrah!, hurrah!'
    line = 'The ants go marching {0} by {0},'.format(count)
    for i in range(2):
        print('{0} {1}'.format(line, hurrah))
    print(line)


def reprise(activity):
    line1 = 'The little one stops to {},'.format(activity)
    line2 = 'And they all go marching down...'
    line3 = 'In the ground...'
    line4 = 'To get out...'
    line5 = 'Of the rain.'

    main_part = '{0}\n{1}\n{2}\n{3}\n{4}'.format(line1, line2, line3, line4, line5)
    print(main_part)


def song(count, activity):
    ants_marching(count)
    reprise(activity)
    boom()


song(count='one', activity='suck his thumb')
song(count='two', activity='tie his shoe')

# 3.
def sphereArea(radius):
    import math
    return 4 * math.pi * radius ** 2


def sphereVolume(radius):
    import math
    return (4 / 3) * math.pi * radius ** 3


def main():
    import math

    print('This program calculates the volume and the surface area')
    print('of a sphere from a given radius.')

    radius = float(input('Enter the radius: '))

    volume = sphereVolume(radius)
    surface_area = sphereArea(radius)

    print('The volume and surface area of a sphere with a radius of')
    print('{} is {:.2f} and {:.2f}, respectively.'.format(radius, volume, surface_area))


main()

# 4.
def sumN(n):
    return n * (n + 1) // 2


def sumNCubes(n):
    return sumN(n) ** 2


def main():
    n = int(input('Please enter a natural number: '))

    sum_of_n = sumN(n)
    sum_of_cubes_n = sumNCubes(n)

    print('The sum of first {0} natural numbers is {1} and'.format(n, sum_of_n), end=' ')
    print('the sum of cubes is {1}.'.format(n, sum_of_cubes_n))


main()

# 5.
def surface_area(radius):
    import math
    return 4 * math.pi * radius ** 2


def cost_per_square(price, surface_area_pizza):
    return price / surface_area_pizza


def main():
    print('This program calculates the cost per square inch of a', end=' ')
    print('pizza given the diameter and the price.')

    diameter = float(input('Enter the diameter: '))
    price = float(input('Enter the price: '))

    surface_area_pizza = surface_area(diameter / 2)
    cost_per_square_pizza = price / surface_area_pizza

    print('The cost per square of a pizza with {} diameter and {}'.format(diameter, price), end=' ')
    print('price is {:.2f}.'.format(cost_per_square_pizza))


main()

# 6.
def calculate_perimeter(a, b, c):
    return a + b + c


def calculate_area(a, b, c):
    perimeter = calculate_perimeter(a, b, c)
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def square(x):
    return x ** 2


def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist


def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    points = []
    for i in range(3):
        p = win.getMouse()
        p.draw(win)
        points.append(p)

    # Use Polygon object to draw the triangle
    triangle = Polygon(points[0], points[1], points[2])
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # side lengths
    a = distance(points[0], points[1])
    b = distance(points[0], points[2])
    c = distance(points[1], points[2])

    # Calculate the perimeter of the triangle
    area = calculate_area(a, b, c)
    message.setText("The area is: {0:0.2f}". format(area))

    # Wait for another click to exit
    win.getMouse()
    win.close()


main()

# 7.
def calculate_nth_fibonacci(n):
    i = 0
    j = 1
    for idx in range(n - 1): # since the above definition is the first term of the series
        j, i = i + j, j

    return j


print(calculate_nth_fibonacci(8))

# 8.
def nextGuess(guess, x):
    return (guess + (x / guess)) / 2


def main(x, n):
    guess = x / 2
    for i in range(n):
        guess = nextGuess(guess, x)

    return guess


print(main(28, 5))

# 9.
def grade(score):
    grade_table = ['F'] * 60 + ['D'] * 10 + ['C'] * 10 + ['B'] * 10 + ['A'] * 10
    return grade_table[score]


print(grade(75))

# 10.
def acronym(text):
    abbreviation = ''
    for word in text.split():
        abbreviation += word[0].upper()

    return abbreviation


print(acronym('Random Access Memory'))

# 11.
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


nums = [1, 2, 3, 4, 5]
squareEach(nums)

print(nums)

# 12.
def sumList(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]

    return total


nums = [1, 2, 3, 4, 5]
print(sumList(nums))

# 13.
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])


strList = ['1', '2', '3', '4', '5']
toNumbers(strList)
print(strList)

# 14.
def main():
    file = askopenfile()
    strList = file.readlines()

    toNumbers(strList)
    squareEach(strList)

    return sumList(strList)


print(main())

# 15.
def drawFace(center, size, win):
    centerX = center.getX()
    centerY = center.getY()
    head = Circle(Point(centerX, centerY), size)
    left_eye = Circle(Point(centerX - size/4, centerY - size/2), size/5)
    right_eye = Circle(Point(centerX + size/4, centerY - size/2), size/5)
    lips_oval = Oval(Point(centerX - size/3, centerY + size/3), Point(centerX + size/3, centerY + size/2))

    for shape in [head, left_eye, right_eye, lips_oval]:
        shape.draw(win)


win = GraphWin('', 640, 320)
drawFace(Point(150, 320), 150, win)
drawFace(Point(20, 30), 10, win)
drawFace(Point(500, 200), 50, win)
win.getMouse()
win.close()

# 16.
def square(x):
    return x ** 2


def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist


def draw_face(center, size, win):
    centerX = center.getX()
    centerY = center.getY()
    head = Circle(Point(centerX, centerY), size)
    head.setFill('white')
    left_eye = Circle(Point(centerX - size / 4, centerY + size / 2), size / 5)
    left_eye.setFill('black')
    right_eye = Circle(Point(centerX + size / 4, centerY + size / 2), size / 5)
    right_eye.setFill('black')
    lips_oval = Oval(Point(centerX - size / 3, centerY - size / 3), Point(centerX + size / 3, centerY - size / 2))

    for shape in [head, left_eye, right_eye, lips_oval]:
        shape.draw(win)


def read_image():
    image_file = input('Please! Enter the filename (only .png files): ')
    image = Image(Point(0, 0), image_file)
    return image


def draw_message_box(win):
    # draw a rectangular for displaying the message
    r = Rectangle(Point(-0.4, -0.1), Point(0.4, 0.1))
    r.setFill('gray')
    r.draw(win)

    return r


def draw_input_message_and_box(win):
    message = Text(Point(-0.1, 0), 'How many faces are to be blocked? ')
    message.setSize(14)
    message.setTextColor('white')
    message.draw(win)

    input_box = Entry(Point(0.15, 0), 3)
    input_box.setText('5')
    input_box.draw(win)

    return message, input_box


def draw_button(win):
    button = Text(Point(0.22, 0), 'OK')
    button.setTextColor('white')
    button.draw(win)
    button_wrapper = Rectangle(Point(0.20, -0.025), Point(0.24, 0.025))
    button_wrapper.draw(win)

    return button, button_wrapper


def draw_attention_message(win):
    attention = Text(Point(-0.1, 0), 'For each face, select two points (i.e. center and edge points)')
    attention.setSize(14)
    attention.setTextColor('white')
    attention.draw(win)

    return attention


def remove_item(item):
    item.undraw()


def main():
    image = read_image()
    width = image.getWidth()
    height = image.getHeight()

    # draw canvas
    win = GraphWin('Photo Anonymizer', width, height)
    win.setCoords(-1, -1, 1, 1)
    image.draw(win)

    r = draw_message_box(win)
    message, input_box = draw_input_message_and_box(win)
    button, button_wrapper = draw_button(win)

    win.getMouse()

    n = int(input_box.getText())

    for item in [message, input_box]:
        remove_item(item)

    attention = draw_attention_message(win)

    win.getMouse()

    for item in [r, attention, button, button_wrapper]:
        remove_item(item)

    for i in range(n):
        center = win.getMouse()
        edge = win.getMouse()
        radius = distance(center, edge)
        draw_face(center, radius, win)

    win.getMouse()


main()

# 17.
def moveTo(shape, center):
    old_center = shape.getCenter()
    old_x = old_center.getX()
    old_y = old_center.getY()

    x = center.getX()
    y = center.getY()

    dx = x - old_x
    dy = y - old_y

    shape.move(dx, dy)

    return shape


def draw_canvas(weight, height):
    win = GraphWin('Moving Circle', weight, height)
    win.setCoords(-1, -1, 1, 1)

    return win


def draw_circle(win, radius):
    p = Point(0, 0)
    c = Circle(p, radius)

    c.draw(win)

    return c


def main():
    win = draw_canvas(640, 640)
    c = draw_circle(win, 0.3)

    for i in range(10):
        center = win.getMouse()
        c = moveTo(c, center)

    win.getMouse()


main()