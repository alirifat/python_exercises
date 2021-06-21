# Chapter 4

# Review Questions (True/False)
# 1. False. Using graphics.py allows to draw graphics by a Python shell. The graphs will appear in a separate window.

# 2. True.

# 3. True. It is the abbreviation of 'picture elements'.

# 4. False. It is called as constructor.

# 5. True.

# 6. False. It moves the x coordinate by 10 points and the y coordinate by 20 points.

# 7. True.

# 8. False. The clone method returns a copy of a graphics object.

# 9. False. It is the default parameter. However, it is possible to pass a different title.

# 10. False. It is getMouse() method.


# Multiple Choice
# 1. D (accessor)
# 2. B (mutator)
# 3. D (Rectangle)
# 4. C (win.setcoords(0, 0, 10, 10)
# 5. D (Line(Point(2,3), Point(4,5))
# 6. D (shape.draw(win))
# 7. D (abs(p1.getX() - p2.getX())
# 8. B (Entry)
# 9. A (GUI)
# 10. B (cyan)


# Discussion
# 1. For example, let's talk about my car. It has the following attributes: the number of tires, the volume of the
# engine, the color, the body configuration (hatchback, sedan, ...) etc. Also, it has the following methods: start(),
# which starts the car; accelerate(), which increase the speed of the car etc.

# 2. a) It produces a point the graph, which located at the coordinates (x = 130 and y = 130).
# 2. b) It draws a circle where its center is located at the point (x = 30 and y = 40). It has a radius of 25 pixels.
# It is filled with blue color and has red color on the outline.
# 2. c) It draws a rectangle where the lower-left corner at the point (x = 20 and y = 20) and the upper-right corner at
# the point (x = 40 and y = 40). It is filled with spring green and has a 3-pixel wide outline.
# 2. d) It is a line from point (x = 100 and y = 100) to point (x = 100 and y = 200). It is red and has an arrow-head
# on the left-side.
# 2. e) It is an oval, where the bounding box is located at the lower-left corner (x = 50 and y = 50) and the upper-
# right corner (x = 60 and y = 100).
# 2. f) It is a square filled with orange.
# 2. g) It is a text located at the point (x = 100 and y = 100). It says 'Hello World!' with courier family font, 16
# font size and italic shape.

# 3. It draws a circle whose center is located at point (x = 50 and y = 50) and the radius is 20. It is filled with red
# and has red outline. Then the program goes into a loop which ask user to click a point on the graph. It then takes the
# coordinates of the user-clicked point and calculates the differences in the x and y coordinates with the circle.
# Then, it moves the circle by the difference. It repeats it 10 times and closes the graph.


# # Programming Exercises
from graphics import *

# 1. a)
def main():
    win = GraphWin()
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)

    win.close()


main()


# 1. b)
def main():
    win = GraphWin()
    centerX = 50
    centerY = 50
    side_length = 20
    shape = Rectangle(Point(centerX, centerY), Point(centerX + side_length, centerY + side_length))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        pX = p.getX()
        pY = p.getY()
        other = Rectangle(Point(pX - side_length / 2, pY - side_length / 2),
                          Point(pX + side_length / 2, pY + side_length / 2))
        other.setFill('red')
        other.setOutline('red')
        other.draw(win)

    win.close()


main()


# 1. c)
def main():
    win = GraphWin(width=640, height=320)
    centerX = 50
    centerY = 50
    side_length = 20
    shape = Rectangle(Point(centerX, centerY), Point(centerX + side_length, centerY + side_length))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        pX = p.getX()
        pY = p.getY()
        other = Rectangle(Point(pX - side_length / 2, pY - side_length / 2),
                          Point(pX + side_length / 2, pY + side_length / 2))
        other.setFill('red')
        other.setOutline('red')
        other.draw(win)

    message = Text(Point(320, 160), 'Click again to quit')
    message.draw(win)
    win.getMouse()
    win.close()


main()


# 2.
def main():
    win = GraphWin(width=640, height=320)
    center_point = Point(320, 160)
    radius = 20

    # the white circle - outer
    white_circle = Circle(center_point, radius * 5)
    white_circle.setFill('white')
    white_circle.draw(win)

    # the black circle
    black_circle = Circle(center_point, radius * 4)
    black_circle.setFill('black')
    black_circle.draw(win)

    # the blue circle
    blue_circle = Circle(center_point, radius * 3)
    blue_circle.setFill('blue')
    blue_circle.draw(win)

    # the red circle
    red_circle = Circle(center_point, radius * 2)
    red_circle.setFill('red')
    red_circle.draw(win)

    # the yellow circle - inner
    yellow_circle = Circle(center_point, radius)
    yellow_circle.setFill('yellow')
    yellow_circle.draw(win)

    win.getMouse()
    win.close()


main()


# 3.
def main():
    win = GraphWin(width=640, height=320)
    centerX = 320
    centerY = 160
    head = Circle(Point(centerX, centerY), 150)
    left_eye = Circle(Point(centerX - 40, centerY - 70), 30)
    right_eye = Circle(Point(centerX + 40, centerY - 70), 30)
    lips_oval = Oval(Point(centerX - 50, centerY + 50), Point(centerX + 50, centerY + 70))

    for shape in [head, left_eye, right_eye, lips_oval]:
        shape.draw(win)

    win.getMouse()
    win.close()


main()


# 4.
def main():
    win = GraphWin(width=640, height=320)

    tree_trunk = Rectangle(Point(130, 320), Point(170, 220))
    tree_trunk.setFill('brown')
    tree_trunk.draw(win)

    for i in range(6):
        leaves = Polygon(Point(30, 220 - (30 * i)),
                         Point(270, 220 - (30 * i)),
                         Point(150, 150 - (30 * i)))
        leaves.setFill('green')
        leaves.draw(win)

    # construct the snowman
    snowman_left_arm = Polygon(Point(320, 210), Point(315, 190), Point(435, 200), Point(430, 220))
    snowman_left_arm.setFill('brown')
    snowman_left_arm.draw(win)

    snowman_right_arm = snowman_left_arm.clone()
    snowman_right_arm.move(145, 0)
    snowman_right_arm.draw(win)

    snowman_trunk = Circle(Point(445, 240), 80)
    snowman_trunk.setFill('white')
    snowman_trunk.draw(win)

    snowman_head = Circle(Point(445, 120), 40)
    snowman_head.setFill('white')
    snowman_head.draw(win)

    snowman_left_eye = Circle(Point(435, 110), 5)
    snowman_left_eye.setFill('black')
    snowman_right_eye = snowman_left_eye.clone()
    snowman_right_eye.move(20, 0)
    snowman_left_eye.draw(win)
    snowman_right_eye.draw(win)

    for i in range(3):
        stone = Circle(Point(445, 280 - (40 * i)), 5)
        stone.setFill('black')
        stone.draw(win)

    win.getMouse()
    win.close()


main()


# 5.
def main():
    win = GraphWin(width=640, height=320)

    left_margin = 30
    right_margin = 30
    upper_margin = 110
    side_length = 100
    distance_between_dices = 20

    for i in range(5):
        dice = Rectangle(Point(left_margin + i * (side_length + distance_between_dices),
                               side_length + upper_margin),
                         Point(left_margin + side_length + i * (side_length + distance_between_dices),
                               upper_margin))
        dice.setFill('white')
        dice.draw(win)

    # draw the top left dots
    radius = 8
    margin_to_the_side = 20

    for i in range(5):
        c = Circle(Point(left_margin + margin_to_the_side + i * (side_length + distance_between_dices),
                         upper_margin + margin_to_the_side), radius)
        c.setFill('black')
        c.draw(win)

    # draw the bottom right dots
    for i in range(5):
        c = Circle(Point(left_margin + side_length - margin_to_the_side + i * (side_length + distance_between_dices),
                         upper_margin + side_length - margin_to_the_side), radius)
        c.setFill('black')
        c.draw(win)

    # draw the middle dots
    for i in range(1, 4, 2):
        c = Circle(Point(left_margin + side_length / 2 + i * (side_length + distance_between_dices),
                         upper_margin + side_length / 2), radius)
        c.setFill('black')
        c.draw(win)

    # draw the top right dots
    for i in range(2, 5):
        c = Circle(Point(left_margin + side_length - margin_to_the_side + i * (side_length + distance_between_dices),
                         upper_margin + margin_to_the_side), radius)
        c.setFill('black')
        c.draw(win)

    # draw the bottom left dots
    for i in range(2, 5):
        c = Circle(Point(left_margin + margin_to_the_side + i * (side_length + distance_between_dices),
                         upper_margin + side_length - margin_to_the_side), radius)
        c.setFill('black')
        c.draw(win)

    # draw dots for dice six
    for i in range(2):
        c = Circle(Point(win.width - right_margin - margin_to_the_side - i * (side_length - 2 * margin_to_the_side),
                         upper_margin + side_length / 2), radius)
        c.setFill('black')
        c.draw(win)

    win.getMouse()
    win.close()


main()

# 6.
def main():
    win = GraphWin("Future Value Calculator", 320, 240)

    Text(Point(105, 50),  'Enter the principal amount:     ').draw(win)
    Text(Point(105, 120), 'Enter the annual interest rate: ').draw(win)
    principal = Entry(Point(275, 50), 5)
    principal.setText('1000')
    principal.draw(win)
    interest = Entry(Point(275, 120), 5)
    interest.setText('0.03')
    interest.draw(win)

    button = Text(Point(160, 180), 'Calculate')
    button.draw(win)
    button_wrapper = Rectangle(Point(210, 200), Point(110, 160))
    button_wrapper.draw(win)

    win.getMouse()

    principal = float(principal.getText())
    apr = float(interest.getText())
    win.close()

    win = GraphWin("Future Value Calculator", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' O.OK').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 30),  '10.0K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80),  ' 7.5K').draw(win)

    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    win.getMouse()
    win.close()


main()

# 7.
def main():
    import math

    win = GraphWin('Circle Intersection', 640, 640)
    win.setCoords(-10, -10, 10, 10)

    Text(Point(-3, 3), 'Enter the radius:      ').draw(win)
    Text(Point(-3, -3), 'Enter the y-intercept: ').draw(win)
    radius_entry = Entry(Point(3, 3), 5)
    radius_entry.setText('3')
    radius_entry.draw(win)
    y_entry = Entry(Point(3, -3), 5)
    y_entry.setText('2')
    y_entry.draw(win)

    win.getMouse()
    win.close()

    win = GraphWin('Circle Intersection', 640, 640)
    win.setCoords(-10, -10, 10, 10)

    radius = float(radius_entry.getText())
    y_intercept = float(y_entry.getText())

    x_root_1 = math.sqrt(abs(radius ** 2 - y_intercept ** 2))
    x_root_2 = -1 * x_root_1

    c = Circle(Point(0, 0), radius)
    c.draw(win)

    line = Line(Point(-10, y_intercept), Point(10, y_intercept))
    line.draw(win)

    root_1 = Circle(Point(x_root_1, y_intercept), 0.1)
    root_1.setFill('red')
    root_1.draw(win)

    root_2 = Circle(Point(x_root_2, y_intercept), 0.1)
    root_2.setFill('red')
    root_2.draw(win)

    win.getMouse()

    print('x-intersection (positive root): ', x_root_1)
    print('x-intersection (negative root): ', x_root_2)

    win.close()


main()

# 8.
def main():
    import math
    win = GraphWin('Line Segment Visualizer', width=640, height=320)

    print('Click two points to draw a line segment.')

    p1 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    c1 = Circle(Point(x1, y1), 3)
    c1.setFill('black')
    c1.draw(win)

    p2 = win.getMouse()
    x2 = p2.getX()
    y2 = p2.getY()
    c2 = Circle(Point(x2, y2), 3)
    c2.setFill('black')
    c2.draw(win)

    line = Line(Point(x1, y1), Point(x2, y2))
    line.draw(win)

    midpoint = line.getCenter()
    c_midpoint = Circle(Point(midpoint.getX(), midpoint.getY()), 3)
    c_midpoint.setFill('cyan')
    c_midpoint.draw(win)

    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    slope = (y2 - y1) / (x2 - x1)

    print('The length of the line is', length)
    print('The slope of the line is', slope)

    win.getMouse()
    win.close()


main()

# 9.
def main():
    import math
    win = GraphWin('Rectangle Drawer', width=640, height=320)

    print('Click two points to draw a line segment.')

    p1 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()

    p2 = win.getMouse()
    x2 = p2.getX()
    y2 = p2.getY()

    r = Rectangle(Point(x1, y1), Point(x2, y2))
    r.draw(win)

    length = abs(y2 - y1)
    width = abs(x2 - x1)
    area = length * width

    perimeter = 2 * (length + width)

    print('The area of the rectangle is', area)
    print('The perimeter of the line is', perimeter)

    win.getMouse()
    win.close()


main()

# 10.
def main():
    import math
    win = GraphWin('Triangle Visualizer', width=640, height=320)

    print('Click two points to draw a line segment.')

    p1 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    c1 = Circle(Point(x1, y1), 3)
    c1.setFill('black')
    c1.draw(win)

    p2 = win.getMouse()
    x2 = p2.getX()
    y2 = p2.getY()
    c2 = Circle(Point(x2, y2), 3)
    c2.setFill('black')
    c2.draw(win)

    p3 = win.getMouse()
    x3 = p3.getX()
    y3 = p3.getY()
    c3 = Circle(Point(x3, y3), 3)
    c3.setFill('black')
    c3.draw(win)

    triangle = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    triangle.draw(win)

    side1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    side2 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    side3 = math.sqrt((x2 - x3) ** 2 + (x2 - x3) ** 2)

    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * abs(s - side1) * abs(s - side2) * abs(s - side3))

    print('The area of the triangle is', area)

    win.getMouse()
    win.close()


main()

# 11.
def main():
    win = GraphWin('Five-Click House', width=640, height=320)

    p1 = win.getMouse()
    p2 = win.getMouse()

    r = Rectangle(p1, p2)
    r.draw(win)

    width_house_frame = abs(p1.getX() - p2.getX())
    height_house_frame = abs(p1.getY() - p2.getY())
    door_frame = width_house_frame / 5

    p3 = win.getMouse()
    middle_point_frame = r.getCenter()
    door = Rectangle(Point(p3.getX() - door_frame / 2, middle_point_frame.getY() + height_house_frame / 2),
                     Point(p3.getX() + door_frame / 2, p3.getY()))
    door.draw(win)

    p4 = win.getMouse()
    window_frame = door_frame / 2
    window = Rectangle(Point(p4.getX() - window_frame / 2, p4.getY() - window_frame / 2),
                       Point(p4.getX() + window_frame / 2, p4.getY() + window_frame / 2))
    window.draw(win)

    # base points for the roof
    base1 = Point(middle_point_frame.getX() - width_house_frame / 2, middle_point_frame.getY() - height_house_frame / 2)
    base2 = Point(middle_point_frame.getX() + width_house_frame / 2, middle_point_frame.getY() - height_house_frame / 2)

    p5 = win.getMouse()
    roof = Polygon(base1, base2, p5)
    roof.draw(win)

    win.getMouse()
    win.close()


main()