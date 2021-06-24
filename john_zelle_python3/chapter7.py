# Chapter 7 Exercises

# Review Questions (True/False)
# 1. True.

# 2. False. It is written as '!='.

# 3. True.

# 4. False. It is implemented by using 'if-else'.

# 5. True.

# 6. False. It requires multiple except statements.

# 7. False. It may be handled with if-elif-else.

# 8. False.

# 9. True.

# 10. False. It is controlling if the input is valid.


# Multiple Choice
# 1. C (control structure)
# 2. C (if-elif-else)
# 3. B (Boolean)
# 4. C (__main__)
# 5. B (True, False)
# 6. C (Nesting)
# 7. A (indentation)
# 8. C (tree)
# 9. A (ValueError)
# 10. C (multi-way decision)


# Discussion
# 1. a) A simple decision is made when there is only a single condition to decide. For example, the program is given
# a single condition and it checks if it is true or false, then jumps to the next line of code.
# 1. b) A two-way decision is a control structure for checking if there are two conditions. Python will check the first
# condition if it is true, then it will execute the body. Otherwise, it will move to the second condition.
# 1. c) A multi-way decision is a structure for checking more than two conditions. Python will check each condition
# individually and execute the one that is evaluated as true.

# 2. Try-except is similar to if-else or if-elif-else since it changes the flow of the program. It is mostly like a
# two-way control structure. However, it is syntactically different since there is no condition given to try structure.
# Python will first try the 'try' statement; however, if the program crashes, it will move to the except statement.
# Finally, there may be several except statement to handle different exceptions. However, there may not be several else
# statements in an if variation. If it is the case, Python will throw a SyntaxError.

# 3.
def silly_tree(a, b, c):
    if a > b:
        if b > c:
            print("Spam Please!")
        else:
            print("It's a late parrot!")
    elif b > c:
        print("Cheese Shoppe")
        if a >= c:
            print("Cheddar")
        elif a < b:
            print("Gouda")
        elif c == b:
            print("Swiss")
    else:
        print("Trees")
        if a == b:
            print("Chestnut")
        else:
            print("Larch")
    print('Done')


silly_tree(3, 4, 5)
silly_tree(3, 3, 3)
silly_tree(5, 4, 3)
silly_tree(3, 5, 2)
silly_tree(5, 4, 7)
silly_tree(3, 3, 2)

# Programming Exercises
import math
from graphics import *


# 1.
def total_wage(hours, hourly_rate):
    if hours < 40:
        total = hours * hourly_rate
        return total
    else:
        total = 40 * hourly_rate
        total = total + (hours - 40) * 1.5 * hourly_rate
        return total


print(total_wage(55, 25))


# 2.
def grading(score):
    if score == 5:
        return 'A'
    elif score == 4:
        return 'B'
    elif score == 3:
        return 'C'
    elif score == 2:
        return 'D'
    elif score < 2:
        return 'F'
    else:
        return 'Please! Enter a score between 0 and 5.'


print(grading(3))


# 3.
def grade_100(score):
    if 100 >= score >= 90:
        return 'A'
    elif 89 >= score >= 80:
        return 'B'
    elif 79 >= score >= 70:
        return 'C'
    elif 69 >= score >= 60:
        return 'D'
    elif 59 >= score >= 0:
        return 'F'
    else:
        return 'Please! Enter a score between 0 and 100.'


print(grade_100(83))


# 4.
def classify_students(credits_taken):
    if credits_taken < 7:
        return 'Freshman'
    elif 15 >= credits_taken >= 7:
        return 'Sophomore'
    elif 25 >= credits_taken >= 16:
        return 'Junior'
    else:
        return 'Senior'


print(classify_students(33))


# 5.
def bmi_calculator(weight, height):
    bmi = weight * 720 / (height ** 2)
    if bmi > 25:
        return 'Your BMI is above the healthy range.'
    elif bmi < 19:
        return 'Your BMI is below the healthy range.'
    else:
        return 'Your BMI is within the healthy range.'


print(bmi_calculator(175, 61))


# 6.
def speeding_ticket_calculator(limit, speed):
    if speed > limit:
        fine = 50 + (speed - limit) * 5
        if speed > 90:
            fine += 200
        return 'Speed was illegal. Total fine is ${}.'.format(fine)

    return 'Speed was legal (within the speed limit).'


print(speeding_ticket_calculator(70, 65))
print(speeding_ticket_calculator(55, 105))


# 7.
def check_pm(time):
    if 'PM' in time:
        return True
    return False


def get_hour_time(time):
    hour_and_minute = time.split()[0].split(':')
    hour, minute = int(hour_and_minute[0]), int(hour_and_minute[1])
    return hour, minute


def to_minute(hours, minutes):
    return hours * 60 + minutes


def calculate_total(hourly_rate, minute):
    return (hourly_rate * minute) / 60


def babysitter_charger(starting_time, ending_time):
    start_hour, start_minute = get_hour_time(starting_time)
    end_hour, end_minute = get_hour_time(ending_time)

    if check_pm(starting_time):
        start_hour += 12

    if check_pm(ending_time):
        end_hour += 12

    ending_total_minutes = to_minute(end_hour, end_minute)
    starting_total_minutes = to_minute(start_hour, start_minute)

    minutes_for_rate_change = to_minute(21, 0)

    if ending_total_minutes > minutes_for_rate_change:  # total minutes until 9:00 PM
        minutes_from_discounted_rate = ending_total_minutes - minutes_for_rate_change
        total_rate_2 = calculate_total(1.75, minutes_from_discounted_rate)

        minutes_from_regular_rate = ending_total_minutes - starting_total_minutes - minutes_from_discounted_rate
        total_rate_1 = calculate_total(2.50, minutes_from_regular_rate)

        return total_rate_1 + total_rate_2

    minutes_from_regular_rate = ending_total_minutes - starting_total_minutes
    return calculate_total(2.50, minutes_from_regular_rate)


print(babysitter_charger('9:00 AM', '9:25 PM'))


# 8.
def is_eligible(age, years_of_citizenship):
    if age >= 25 and years_of_citizenship >= 7:
        if age >= 30 and years_of_citizenship >= 9:
            return 'Eligible for both House and Senate.'
        return 'Only eligible for House.'
    return 'Not eligible for House or Senate.'


print(is_eligible(43, 11))  # both
print(is_eligible(38, 8))  # only house
print(is_eligible(28, 10))  # only house
print(is_eligible(26, 5))  # neither


# 9.
def when_is_easter(year):
    if 2048 >= year >= 1982:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7

        date = 22 + d + e
        if date > 31:
            return 'April {0}, {1}'.format(date % 31, year)
        else:
            return 'March {0}, {1}'.format(date, year)
    return 'Year should be within the range of 1982 - 2048, including.'


print(when_is_easter(2022))
print(when_is_easter(2049))
print(when_is_easter(1999))


# 10.
def when_is_easter_modified(year):
    if 2099 >= year >= 1900:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7

        date = 22 + d + e

        if year in [1954, 1981, 2049, 2076]:
            date = date - 7

        if date > 31:
            return 'April {0}, {1}'.format(date % 31, year)
        else:
            return 'March {0}, {1}'.format(date, year)

    return 'Year should be within the range of 1900 - 2099, including.'


print(when_is_easter_modified(1954))


# 11.
def is_century(year):
    if year % 100 == 0:
        return True
    return False


def is_leap_year(year):
    if is_century(year):
        if year % 400 == 0:
            return True
    else:
        if year % 4 == 0:
            return True
    return False


print(is_leap_year(1900))
print(is_leap_year(2012))


# 12.
def get_month_day_year(date):
    month_day_year = date.split('/')
    month, day, year = int(month_day_year[0]), int(month_day_year[1]), int(month_day_year[2])
    return month, day, year


def is_valid_date(date):
    month, day, year = get_month_day_year(date)

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 12:
        if is_leap_year(year) and month == 2:
            if day <= days[month - 1] + 1:  # accounts for extra day in February
                return True
        if day <= days[month - 1]:
            return True
    return False


print(is_valid_date('02/29/2012'))
print(is_valid_date('02/30/2012'))


# 13.
def day_of_year(date):
    if is_valid_date(date):
        month, day, year = get_month_day_year(date)
        day_num = 31 * (month - 1) + day
        if month > 2 and is_leap_year(year):
            day_num += 1
        if month > 2:
            day_num -= (4 * month + 23) // 10
        return day_num
    return False


print('checking day_of_year function:')
print(day_of_year('01/15/2017') == 15)
print(day_of_year('02/23/2019') == 54)
print(day_of_year('03/02/2020') == 62)


# 14.
def main():
    import math

    win = GraphWin('Circle Intersection', 640, 640)
    win.setCoords(-10, -10, 10, 10)

    message1 = Text(Point(-3, 3), 'Enter the radius:      ')
    message1.draw(win)

    message2 = Text(Point(-3, -3), 'Enter the y-intercept: ')
    message2.draw(win)

    radius_entry = Entry(Point(3, 3), 5)
    radius_entry.setText('3')
    radius_entry.draw(win)

    y_entry = Entry(Point(3, -3), 5)
    y_entry.setText('2')
    y_entry.draw(win)

    win.getMouse()

    message1.undraw()
    message2.undraw()
    radius_entry.undraw()
    y_entry.undraw()

    radius = float(radius_entry.getText())
    c = Circle(Point(0, 0), radius)
    c.draw(win)

    y_intercept = float(y_entry.getText())
    x_root_1 = math.sqrt(abs(radius ** 2 - y_intercept ** 2))
    x_root_2 = -1 * x_root_1

    line = Line(Point(-10, y_intercept), Point(10, y_intercept))
    line.draw(win)

    if x_root_1 <= radius:
        root_1 = Circle(Point(x_root_1, y_intercept), 0.1)
        root_2 = Circle(Point(x_root_2, y_intercept), 0.1)

        for shape in [root_1, root_2]:
            shape.setFill('red')
            shape.draw(win)

        print('x-intersection (positive root): ', x_root_1)
        print('x-intersection (negative root): ', x_root_2)

    print("The line doesn't intersect with the circle.")
    win.getMouse()
    win.close()


main()


# 15.
def get_x_y(win):
    p = win.getMouse()
    x, y = p.getX(), p.getY()
    return x, y


def draw_point(win, x, y, color):
    c = Circle(Point(x, y), 3)
    c.setFill(color)
    c.draw(win)
    return c


def main():
    import math
    win = GraphWin('Line Segment Visualizer', width=640, height=320)

    print('Click two points to draw a line segment.')

    x1, y1 = get_x_y(win)
    c1 = draw_point(win, x1, y1, 'black')

    x2, y2 = get_x_y(win)
    c2 = draw_point(win, x2, y2, 'black')

    line = Line(Point(x1, y1), Point(x2, y2))
    line.draw(win)

    midpoint = line.getCenter()
    c3 = draw_point(win, midpoint.getX(), midpoint.getY(), 'cyan')

    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print('The length of the line is', length)

    try:
        slope = (y2 - y1) / (x2 - x1)
        print('The slope of the line is', slope)
    except ZeroDivisionError:
        print("Vertical lines don't have a slope.")

    win.getMouse()
    win.close()


main()


# 16.
def square(x):
    return x ** 2


def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist


def main():
    win = GraphWin(width=640, height=640)
    win.setCoords(-8, -8, 8, 8)
    center = Point(0, 0)

    colors = ['yellow', 'red', 'blue', 'black', 'white']
    for i in range(5, 0, -1):
        c = Circle(center, i)
        c.setFill(colors[i - 1])
        c.draw(win)

    total_score = 0
    for i in range(5):
        p = win.getMouse()
        radius = distance(center, p)

        if radius < 5:
            score = 9 - 2 * int(radius)
        else:
            score = 0

        print(score)
        total_score += score

    r = Rectangle(Point(-4, -0.5), Point(4, 0.5))
    r.setFill('gray')
    r.draw(win)

    message = Text(center, 'Total score: {}'.format(total_score))
    message.setTextColor('white')
    message.draw(win)

    win.getMouse()
    win.close()


main()


# 17.
def get_x_y(shape):
    center = shape.getCenter()
    x = center.getX()
    y = center.getY()
    return x, y


def beyond(coordinate, radius, limit):
    return coordinate + radius > limit


def away(coordinate, radius):
    return coordinate - radius < 0


def is_on_edge(shape, width, height):
    x, y = get_x_y(shape)
    radius = shape.getRadius()

    if not beyond(x, radius, width) and not away(x, radius) and not beyond(y, radius, height) and not away(y, radius):
        return False
    return True


def bouncing_circle(width, height, radius):
    win = GraphWin('Bouncing Circle', width, height)
    c = Circle(Point(320, 240), radius)
    c.draw(win)

    dx = 1
    dy = 1
    for i in range(10000):
        if not is_on_edge(c, width, height):
            c.move(dx, dy)
        else:
            x, y = get_x_y(c)

            if beyond(x, radius, width):
                dx = -1
            elif away(x, radius):
                dx = 1
            elif beyond(y, radius, height):
                dy = -1
            elif away(y, radius):
                dy = 1

            c.move(dx, dy)
        update(30)

    win.getMouse()


bouncing_circle(640, 480, 20)


# 18.
def grading(score):
    if 100 >= score >= 90:
        return 'A'
    elif 89 >= score >= 80:
        return 'B'
    elif 79 >= score >= 70:
        return 'C'
    elif 69 >= score >= 60:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Please! Enter a score between 0 and 100.'


print(grading(85))
print(grading(101))