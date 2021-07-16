# Chapter 10 Exercises

# Review Questions (True/False)
# 1. True.

# 2. False. They are called as methods.

# 3. False. It is self.

# 4. False.

# 5. False. It is record.

# 6. True.

# 7. False.

# 8. False.

# 9. False.

# 10. True.


# Multiple Choice
# 1. B (class)
# 2. A (three)
# 3. D (function definition)
# 4. B (self.x)
# 5. C (an undercore(_))
# 6. D (encapsulation)
# 7. C (""")
# 8. A (bool)
# 9. C (setLabel)
# 10. C (setValue)


# Discussion
# 1. An instance variable is very similar to a function variable except that the function variables are local; thus,
# they cannot be accessed outside of the function. However, instance variable can be accessed outside of the methods.

# 2.
# a) A method is a function inside a class.
# b) An instance variable is an attribute of an object which contains data.
# c) A constructor generates a new object based on class attributes.
# d) An accessor helps to access instance variables.
# e) A mutator manipulates the instance variables.

# # 3.
# class Bozo:
#
#     def __init__(self, value):
#         print('Creating a Bozo from:', value)
#         self.value = 2 * value
#
#     def clown(self, x):
#         print('Clowning:', x)
#         print(x * self.value)
#         return x + self.value
#
#
# def main():
#     print('Clowning around now.')
#     c1 = Bozo(3)
#     c2 = Bozo(4)
#     print(c1.clown(3))
#     print(c2.clown(c1.clown(2)))
#
#
# main()

# Programming Exercises
# # 1.
# from graphics import *
# from math import radians, cos, sin
#
# class Button:
#     """A button is a labeled rectangle in a window .
#     It is activated or deactivated with the activate()
#     and deactivate() methods. The clicked (p) method
#     returns true if the button is active and p is inside it."""
#
#     def __init__(self, win, center, width, height, label):
#         """ Creates a rectangular button, eg:
#         qb = Button(my_win, center_point, width, height, 'Quit') """
#
#         w, h = width / 2.0, height / 2.0
#         x, y = center.getX(), center.getY()
#         self.x_max, self.x_min = x + w, x - w
#         self.y_max, self.y_min = y + h, y - h
#         p1 = Point(self.x_min, self.y_min)
#         p2 = Point(self.x_max, self.y_max)
#         self.rect = Rectangle(p1, p2)
#         self.rect.setFill('lightgray')
#         self.rect.draw(win)
#         self.label = Text(center, label)
#         self.label.draw(win)
#         self.deactivate()
#
#     def clicked(self, p):
#         """ Returns True if button active and p is inside """
#         return self.active and self.x_min <= p.getX() <= self.x_max and self.y_min <= p.getY() <= self.y_max
#
#     def get_label(self):
#         """ Returns the label string of this button. """
#         return self.label.getText()
#
#     def activate(self):
#         """ Sets this button to 'active'. """
#         self.label.setFill('black')
#         self.rect.setWidth(2)
#         self.active = True
#
#     def deactivate(self):
#         """ Sets this button to 'inactive'. """
#         self.label.setFill('darkgrey')
#         self.rect.setWidth(1)
#         self.active = False
#
#     def undraw(self):
#         self.rect.undraw()
#         self.label.undraw()
#
#
# class Projectile:
#     """ Simulates the flight of simple projectiles near the earth's
#     surface, ignoring wind resistance. Tracking is done in two
#     dimensions, height (y) and distance (x). """
#
#     def __init__(self, angle, velocity, height):
#         """ Create a projectile with given launch angle, initial
#         velocity and height. """
#         self.x_pos = 0.0
#         self.y_pos = height
#         theta = radians(angle)
#         self.x_vel = velocity * cos(theta)
#         self.y_vel = velocity * sin(theta)
#
#     def update(self, time):
#         """ Update the state of this projectile to move it time seconds
#         farther into its flight. """
#         self.x_pos = self.x_pos + time * self.x_vel
#         y_vel1 = self.y_vel - 9.8 * time
#         self.y_pos = self.y_pos + time * (self.y_vel + y_vel1) / 2.0
#         self.y_vel = y_vel1
#
#     def get_y(self):
#         """" Returns the y position (height) of this projectile. """
#         return self.y_pos
#
#     def get_x(self):
#         """ Returns the x position (distance) of this projectile. """
#         return self.x_pos
#
#
# class ShotTracker:
#
#     def __init__(self, win, angle, velocity, height):
#         """ win is the GraphWin to display the shot. angle, velocity,
#         and height are initial projectile parameters."""
#
#         self.proj = Projectile(angle, velocity, height)
#         self.marker = Circle(Point(0, height), 3)
#         self.marker.setFill('red')
#         self.marker.setOutline('red')
#         self.marker.draw(win)
#
#     def update(self, dt):
#         """ Move the shot dt seconds farther along its flight. """
#
#         # update the projectile
#         self.proj.update(dt)
#
#         # move the circle to the new projectile location
#         center = self.marker.getCenter()
#         dx = self.proj.get_x() - center.getX()
#         dy = self.proj.get_y() - center.getY()
#         self.marker.move(dx, dy)
#
#     def get_x(self):
#         """ Return the current x coordinate of the shot's center """
#         return self.proj.get_x()
#
#     def get_y(self):
#         """ Return the current y coordinate of the shot's center """
#         return self.proj.get_y()
#
#     def undraw(self):
#         """ Undraw the shot. """
#         self.marker.undraw()
#
#
# class InputDialog:
#     """ A custom window for getting simulation values (angle, velocity,
#     and height) from the user. """
#
#     def __init__(self, angle, vel, height):
#         """ Build and display the input window. """
#
#         self.win = win = GraphWin('Initial Values', 200, 300)
#         win.setCoords(0, 4.5, 4, 0.5)
#
#         Text(Point(1, 1), 'Angle').draw(win)
#         self.angle = Entry(Point(3, 1), 5).draw(win)
#         self.angle.setText(str(angle))
#
#         Text(Point(1, 2), 'Velocity').draw(win)
#         self.vel = Entry(Point(3, 2), 5).draw(win)
#         self.vel.setText(str(vel))
#
#         Text(Point(1, 3), 'Height').draw(win)
#         self.height = Entry(Point(3, 3), 5).draw(win)
#         self.height.setText(str(height))
#
#         self.fire = Button(win, Point(1, 4), 1.25, 0.5, 'Fire!')
#         self.fire.activate()
#
#         self.quit = Button(win, Point(3, 4), 1.25, 0.5, 'Quit')
#         self.quit.activate()
#
#     def interact(self):
#         """ Wait for user to click Quit or Fire buttons.
#         Returns a string indicating which button was clicked. """
#
#         while True:
#             pt = self.win.getMouse()
#             if self.quit.clicked(pt):
#                 return 'Quit'
#             if self.fire.clicked(pt):
#                 return 'Fire!'
#
#     def get_values(self):
#         """ Return input values. """
#
#         a = float(self.angle.getText())
#         v = float(self.vel.getText())
#         h = float(self.height.getText())
#         return a, v, h
#
#
# def main():
#
#     # create animation window
#     win = GraphWin('Projectile Animation', 640, 480, autoflush=False)
#     win.setCoords(-10, -10, 210, 155)
#
#     # draw baseline
#     Line(Point(-10, 0), Point(210, 0)).draw(win)
#
#     # draw labeled ticks every 50 meters
#     for x in range(0, 210, 50):
#         Text(Point(x, -5), str(x)).draw(win)
#         Line(Point(x, 0), Point(x, 2)).draw(win)
#
#     # event loop, each time through fires a single shot
#     angle, vel, height = 45.0, 40.0, 2.0
#     while True:
#         # interact with the user
#         input_win = InputDialog(angle, vel, height)
#         choice = input_win.interact()
#         input_win.win.close()
#
#         if choice == 'Quit': # loop exit
#             break
#
#         # create a shot and track until it hits ground or leaves window
#         angle, vel, height = input_win.get_values()
#         shot = ShotTracker(win, angle, vel, height)
#         max_height = 0
#         while 0 <= shot.get_y() and -10 < shot.get_x() <= 210:
#             if max_height < shot.get_y():
#                 max_height = shot.get_y()
#
#             shot.update(1/50)
#             update(50)
#
#         text = 'The maximum height achieved by the cannonball: {0:0.2f} m.'.format(max_height)
#         goodbye_message = Button(win, Point(100, 72), 150, 20, text)
#         goodbye_message.activate()
#
#         while True:
#             pt = win.getMouse()
#             if goodbye_message.clicked(pt):
#                 goodbye_message.undraw()
#                 break
#
#     win.close()
#
#
# main()
#
# # 2.
# from graphics import *
# class Button:
#     """A button is a labeled rectangle in a window .
#     It is activated or deactivated with the activate()
#     and deactivate() methods. The clicked (p) method
#     returns true if the button is active and p is inside it."""
#
#     def __init__(self, win, center, width, height, label):
#         """ Creates a rectangular button, eg:
#         qb = Button(my_win, center_point, width, height, 'Quit') """
#
#         w, h = width / 2.0, height / 2.0
#         x, y = center.getX(), center.getY()
#         self.x_max, self.x_min = x + w, x - w
#         self.y_max, self.y_min = y + h, y - h
#         p1 = Point(self.x_min, self.y_min)
#         p2 = Point(self.x_max, self.y_max)
#         self.rect = Rectangle(p1, p2)
#         self.rect.setFill('lightgray')
#         self.rect.draw(win)
#         self.label = Text(center, label)
#         self.label.draw(win)
#         self.deactivate()
#
#     def clicked(self, p):
#         """ Returns True if button active and p is inside """
#         return self.active and self.x_min <= p.getX() <= self.x_max and self.y_min <= p.getY() <= self.y_max
#
#     def get_label(self):
#         """ Returns the label string of this button. """
#         return self.label.getText()
#
#     def activate(self):
#         """ Sets this button to 'active'. """
#         self.label.setFill('black')
#         self.rect.setWidth(2)
#         self.active = True
#
#     def deactivate(self):
#         """ Sets this button to 'inactive'. """
#         self.label.setFill('darkgrey')
#         self.rect.setWidth(1)
#         self.active = False
#
#     def undraw(self):
#         self.rect.undraw()
#         self.label.undraw()
#
#
# class Marker:
#     """ A circle to represent data points. """
#
#     def __init__(self, win, radius, color='black'):
#         self.win = win
#         self.radius = radius
#         self.color = color
#         self.markers = []
#         self.total_x = 0
#         self.total_y = 0
#         self.x_square_total = 0
#         self.sum_xy = 0
#
#     def draw(self, center):
#         c = Circle(center, self.radius)
#         c.setFill(self.color)
#         c.draw(self.win)
#         self.markers.append(c)
#
#     def undraw(self):
#         self.markers[-1].undraw()
#         self.markers.pop()
#
#     def _get_axis_total(self, axis):
#         total = 0
#         for c in self.markers:
#             if axis == 'x':
#                 temp = c.getCenter().getX()
#             elif axis == 'y':
#                 temp = c.getCenter().getY()
#             elif axis == 'xy':
#                 x = c.getCenter().getX()
#                 y = c.getCenter().getY()
#                 temp = x * y
#             total += temp
#         return total
#
#     def _square_total_x(self):
#         total = 0
#         for c in self.markers:
#             x = c.getCenter().getX()
#             total += x ** 2
#         return total
#
#     def _get_n(self):
#         return len(self.markers)
#
#     def get_parameters(self):
#         x_bar = self._get_axis_total(axis='x') / self._get_n()
#         y_bar = self._get_axis_total(axis='y') / self._get_n()
#
#         nominator = (self._get_axis_total(axis='xy') - self._get_n() * x_bar * y_bar)
#         denominator = (self._square_total_x() - self._get_n() * (x_bar ** 2))
#         m = nominator / denominator
#
#         return x_bar, y_bar, m
#
#
# class RLine:
#     """ Draws the regression line. The default color is red. """
#
#     def __init__(self, win, x_bar, y_bar, m, left_edge, right_edge, color='red'):
#         self.win = win
#         self.x_bar = x_bar
#         self.y_bar = y_bar
#         self.m = m
#         self.left_edge = left_edge
#         self.right_edge = right_edge
#         self.color = color
#
#     def _calculate_end_point_y_axis(self, edge):
#         if edge == 'left':
#             return self.y_bar + self.m * (self.left_edge - self.x_bar)
#         elif edge == 'right':
#             return self.y_bar + self.m * (self.right_edge - self.x_bar)
#
#     def draw(self):
#         left_y_point = self._calculate_end_point_y_axis(edge='left')
#         right_y_point = self._calculate_end_point_y_axis(edge='right')
#         l = Line(Point(self.left_edge, left_y_point), Point(self.right_edge, right_y_point))
#         l.setFill(self.color)
#         l.draw(self.win)
#
#
# def regression_plot(width, height):
#     win = GraphWin('Regression Plot', width, height)
#     win.setCoords(-10, -10, 10, 10)
#
#     welcome_text = 'Please! Click on the graph to locate the data points.'
#     welcome_button = Button(win, Point(0, 0), 12, 2, welcome_text)
#     welcome_button.activate()
#
#     start_button = Button(win, Point(0, -2), 4, 1, 'Start!')
#     start_button.activate()
#
#     exit_button = Button(win, Point(8, -9.5), 4, 1, 'Quit!')
#     exit_button.deactivate()
#
#     done_button = Button(win, Point(-8, -9.5), 4, 1, 'Done!')
#     done_button.deactivate()
#
#     radius = 0.1
#     m = Marker(win, radius)
#     while True:
#         pt = win.getMouse()
#
#         if start_button.clicked(pt):
#             start_button.undraw()
#             welcome_button.undraw()
#             exit_button.activate()
#             done_button.activate()
#             break
#
#     while True:
#         pt = win.getMouse()
#
#         m.draw(pt)
#
#         if exit_button.clicked(pt):
#             m.undraw()
#             sure_button = Button(win, Point(0, 0), 12, 2, 'Are you sure you want to stop? ')
#             sure_button.activate()
#
#             yes_button = Button(win, Point(-1.5, -2), 2, 1, 'Yes')
#             yes_button.activate()
#
#             no_button = Button(win, Point(1.5, -2), 2, 1, 'No')
#             no_button.activate()
#
#             while True:
#                 p = win.getMouse()
#
#                 if yes_button.clicked(p):
#                     return
#
#                 elif no_button.clicked(p):
#                     sure_button.undraw()
#                     yes_button.undraw()
#                     no_button.undraw()
#                     break
#
#         if done_button.clicked(pt):
#             m.undraw()
#             break
#
#     x_bar, y_bar, m = m.get_parameters()
#     l = RLine(win, x_bar, y_bar, m, -10, 10)
#     l.draw()
#
#     win.getMouse()
#
#
# regression_plot(640, 480)

# # 3.
# from graphics import *
# from random import sample
# class Button:
#     """A button is a labeled rectangle in a window .
#     It is activated or deactivated with the activate()
#     and deactivate() methods. The clicked (p) method
#     returns true if the button is active and p is inside it."""
#
#     def __init__(self, win, center, width, height, label):
#         """ Creates a rectangular button, eg:
#         qb = Button(my_win, center_point, width, height, 'Quit') """
#
#         w, h = width / 2.0, height / 2.0
#         x, y = center.getX(), center.getY()
#         self.x_max, self.x_min = x + w, x - w
#         self.y_max, self.y_min = y + h, y - h
#         p1 = Point(self.x_min, self.y_min)
#         p2 = Point(self.x_max, self.y_max)
#         self.rect = Rectangle(p1, p2)
#         self.rect.setFill('lightgray')
#         self.rect.draw(win)
#         self.label = Text(center, label)
#         self.label.draw(win)
#         self.deactivate()
#
#     def clicked(self, p):
#         """ Returns True if button active and p is inside """
#         return self.active and self.x_min <= p.getX() <= self.x_max and self.y_min <= p.getY() <= self.y_max
#
#     def get_label(self):
#         """ Returns the label string of this button. """
#         return self.label.getText()
#
#     def activate(self):
#         """ Sets this button to 'active'. """
#         self.label.setFill('black')
#         self.rect.setWidth(2)
#         self.active = True
#
#     def deactivate(self):
#         """ Sets this button to 'inactive'. """
#         self.label.setFill('darkgrey')
#         self.rect.setWidth(1)
#         self.active = False
#
#     def undraw(self):
#         self.rect.undraw()
#         self.label.undraw()
#
#
# def main():
#     win = GraphWin('Three Button Monte!', 640, 480)
#     win.setCoords(-16, -12, 16, 12)
#
#     door1 = Button(win, Point(-9, 1), 6, 9, 'Door 1')
#     door1.activate()
#
#     door2 = Button(win, Point(0, 1), 6, 9, 'Door 2')
#     door2.activate()
#
#     door3 = Button(win, Point(9, 1), 6, 9, 'Door 3')
#     door3.activate()
#
#     welcome_text = Text(Point(0, 8), 'Please! Select a door to start the game.')
#     welcome_text.setSize(16)
#     welcome_text.draw(win)
#
#     prices = sample(['car', 'goat', 'goat'], k=3)
#     while True:
#         pt = win.getMouse()
#
#         if door1.clicked(pt):
#             door_number = 0
#             break
#         if door2.clicked(pt):
#             door_number = 1
#             break
#         if door3.clicked(pt):
#             door_number = 2
#             break
#
#     welcome_text.undraw()
#
#     if prices[door_number] == 'car':
#         message = Text(Point(0, -7), 'You Win!!!')
#         message.setStyle('bold')
#         message.setSize(16)
#         message.draw(win)
#     else:
#         message = Text(Point(0, -7), 'You Lost!')
#         message.draw(win)
#
#     win.getMouse()
#
#
# main()

# # 4.
# from graphics import *
# from random import sample
# class Button:
#     """A button is a labeled rectangle in a window .
#     It is activated or deactivated with the activate()
#     and deactivate() methods. The clicked (p) method
#     returns true if the button is active and p is inside it."""
#
#     def __init__(self, win, center, width, height, label):
#         """ Creates a rectangular button, eg:
#         qb = Button(my_win, center_point, width, height, 'Quit') """
#
#         w, h = width / 2.0, height / 2.0
#         x, y = center.getX(), center.getY()
#         self.x_max, self.x_min = x + w, x - w
#         self.y_max, self.y_min = y + h, y - h
#         p1 = Point(self.x_min, self.y_min)
#         p2 = Point(self.x_max, self.y_max)
#         self.rect = Rectangle(p1, p2)
#         self.rect.setFill('lightgray')
#         self.rect.draw(win)
#         self.label = Text(center, label)
#         self.label.draw(win)
#         self.deactivate()
#
#     def clicked(self, p):
#         """ Returns True if button active and p is inside """
#         return self.active and self.x_min <= p.getX() <= self.x_max and self.y_min <= p.getY() <= self.y_max
#
#     def get_label(self):
#         """ Returns the label string of this button. """
#         return self.label.getText()
#
#     def activate(self):
#         """ Sets this button to 'active'. """
#         self.label.setFill('black')
#         self.rect.setWidth(2)
#         self.active = True
#
#     def deactivate(self):
#         """ Sets this button to 'inactive'. """
#         self.label.setFill('darkgrey')
#         self.rect.setWidth(1)
#         self.active = False
#
#     def undraw(self):
#         self.rect.undraw()
#         self.label.undraw()
#
#
# class Score:
#
#     def __init__(self, win, p, label, size=12):
#         self.win = win
#         self.p = p
#         self.label = label
#         self.size = size
#         self.drawn = False
#
#     def draw(self):
#         message = Text(self.p, self.label)
#         message.setSize(self.size)
#         self.drawn = message.draw(self.win)
#
#     def undraw(self):
#         if self.drawn:
#             self.drawn.undraw()
#
#     def set_value(self, value):
#         self.undraw()
#         self.label = value
#         self.draw()
#
#
# def main():
#     win = GraphWin('Three Button Monte!', 640, 480)
#     win.setCoords(-16, -12, 16, 12)
#
#     wins = 0
#     losses = 0
#     # shows wins and losses
#     win_text = Score(win, Point(-14, 11), 'Wins: ')
#     win_text.draw()
#     win_score = Score(win, Point(-12, 11), str(wins))
#     win_score.draw()
#
#     loss_text = Score(win, Point(-8, 11), 'Losses: ')
#     loss_text.draw()
#     loss_score = Score(win, Point(-6, 11), str(losses))
#     loss_score.draw()
#
#     # doors
#     door1 = Button(win, Point(-9, 0), 6, 9, 'Door 1')
#     door1.activate()
#
#     door2 = Button(win, Point(0, 0), 6, 9, 'Door 2')
#     door2.activate()
#
#     door3 = Button(win, Point(9, 0), 6, 9, 'Door 3')
#     door3.activate()
#
#     quit_button = Button(win, Point(0, -11), 4, 1, 'Quit!')
#     quit_button.activate()
#
#     welcome_text = Text(Point(0, 7), 'Please! Select a door to start the game.')
#     welcome_text.setSize(16)
#     welcome_text.draw(win)
#
#     wins = 0
#     losses = 0
#     while True:
#         prizes = sample(['Car', 'Goat', 'Goat'], k=3)
#
#         while True:
#             p = win.getMouse()
#
#             if door1.clicked(p):
#                 door_number = 0
#                 break
#             if door2.clicked(p):
#                 door_number = 1
#                 break
#             if door3.clicked(p):
#                 door_number = 2
#                 break
#
#             if quit_button.clicked(p):
#                 return
#
#         if prizes[door_number] == 'car':
#             wins += 1
#             win_score.set_value(str(wins))
#
#             message = Score(win, Point(0, -8), 'You Win!!!', 16)
#             message.draw()
#
#         else:
#             losses += 1
#             loss_score.set_value(str(losses))
#
#             message = Score(win, Point(0, -8), 'You Lost!', 16)
#             message.draw()
#
#         prize1 = Score(win, Point(-9, -3), prizes[0])
#         prize1.draw()
#         prize2 = Score(win, Point(0, -3), prizes[1])
#         prize2.draw()
#         prize3 = Score(win, Point(9, -3), prizes[2])
#         prize3.draw()
#
#         win.getMouse()
#         message.undraw()
#         for i in [prize1, prize2, prize3]:
#             i.undraw()
#
#
# main()
#
# # 5.
# class Student:
#
#     def __init__(self):
#         self.credits = 0
#         self.qpoints = 0
#
#     def get_hours(self):
#         return self.credits
#
#     def get_qpoints(self):
#         return self.qpoints
#
#     def add_grade(self, grade_point, credit_taken):
#         self.qpoints += float(grade_point) * float(credit_taken)
#         self.credits += float(credit_taken)
#
#     def gpa(self):
#         return self.qpoints / self.credits
#
#
# def main():
#     new_student = Student()
#     while True:
#         grade_point = input('Please! Enter the grade point (e.g. 3.75) [Press <Enter> to quit]: ')
#
#         if grade_point == '':
#             break
#
#         credit_taken = input(
#             'Please! Enter the number of credit hours for the class (e.g. 3) [Press <Enter> to quit]: ')
#
#         new_student.add_grade(grade_point, credit_taken)
#
#     print('The student has {0:0.2f} GPA.'.format(new_student.gpa()))
#
#
# main()
#
# # 6.
# class Student:
#
#     def __init__(self):
#         self.credits = 0
#         self.qpoints = 0
#
#     def get_hours(self):
#         return self.credits
#
#     def get_qpoints(self):
#         return self.qpoints
#
#     def add_grade(self, grade_point, credit_taken):
#         self.qpoints += float(grade_point) * float(credit_taken)
#         self.credits += float(credit_taken)
#
#     def add_letter_grade(self, grade_letter, credit_taken):
#         if grade_letter == 'A+' or grade_letter == 'A':
#             grade_point = 4
#         elif grade_letter == 'A-':
#             grade_point = 3.7
#         elif grade_letter == 'B+':
#             grade_point = 3.3
#         elif grade_letter == 'B':
#             grade_point = 3
#         elif grade_letter == 'B-':
#             grade_point = 2.7
#         elif grade_letter == 'C+':
#             grade_point = 2.3
#         elif grade_letter == 'C':
#             grade_point = 2
#         elif grade_letter == 'C-':
#             grade_point = 1.7
#         elif grade_letter == 'D+':
#             grade_point = 1.3
#         elif grade_letter == 'D':
#             grade_point = 1
#         elif grade_letter == 'E' or grade_letter == 'F':
#             grade_point = 0
#         else:
#             print('Please! Enter a valid grade.')
#             return -1
#
#         self.add_grade(grade_point, credit_taken)
#
#     def gpa(self):
#         return self.qpoints / self.credits
#
#
# def main():
#     new_student = Student()
#     user_response = input('Would you like to enter grade in (1) points or (2) letters [Press <Enter> to quit]: ')
#     while True:
#         if user_response == '1':
#             while True:
#                 grade_point = input('Please! Enter the grade point (e.g. 3.75) [Press <Enter> to quit]: ')
#                 if grade_point == '':
#                     break
#                 credit_taken = input(
#                     'Please! Enter the number of credit hours for the class (e.g. 3): ')
#                 new_student.add_grade(grade_point, credit_taken)
#             break
#         elif user_response == '2':
#             while True:
#                 grade_letter = input('Please! Enter the grade letter (e.g. A-) [Press <Enter> to quit]: ')
#                 if grade_letter == '':
#                     break
#                 credit_taken = input(
#                     'Please! Enter the number of credit hours for the class (e.g. 3): ')
#                 new_student.add_letter_grade(grade_letter, credit_taken)
#             break
#         elif user_response == '':
#             break
#         else:
#             user_response = input('Please! Enter a valid option (1) point; (2) letter [Press <Enter> to quit]: ')
#
#     print('The student has {0:0.2f} GPA.'.format(new_student.gpa()))
#
#
# main()

# 7.
# See roller_circle_buttons.py

# 8.
# See roller_color_dice.py
#
# # 9.
# from math import pi
# class Sphere:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_radius(self):
#         return self.radius
#
#     def surface_area(self):
#         return 4 * pi * self.radius ** 2
#
#     def volume(self):
#         return (4 / 3) * pi * self.radius ** 3
#
#
# s1 = Sphere(5)
# print(s1.surface_area())
# print(s1.volume())

# # 10.
# class Cube:
#
#     def __init__(self, side_length):
#         self.side_length = side_length
#
#     def get_side_length(self):
#         return self.side_length
#
#     def surface_area(self):
#         return 6 * self.side_length ** 2
#
#     def volume(self):
#         return self.side_length ** 3
#
#
# c1 = Cube(3)
# print(c1.surface_area())
# print(c1.volume())
#
# # 11.
# from random import randint, choice
#
# class PlayingCard:
#
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#
#     def __str__(self):
#         if self.rank == 1:
#             rank_string = 'Ace'
#         elif self.rank == 11:
#             rank_string = 'Jack'
#         elif self.rank == 12:
#             rank_string = 'Queen'
#         elif self.rank == 13:
#             rank_string = 'King'
#         else:
#             rank_string = self.rank
#
#         if self.suit == 's':
#             suit_string = 'Spades'
#         elif self.suit == 'h':
#             suit_string = 'Hearts'
#         elif self.suit == 'c':
#             suit_string = 'Clubs'
#         elif self.suit == 'd':
#             suit_string = 'Diamonds'
#
#         return '{0} of {1}'.format(rank_string, suit_string)
#
#     def get_rank(self):
#         return self.rank
#
#     def get_suit(self):
#         return self.suit
#
#     def value(self):
#         if self.rank > 10:
#             return 10
#         else:
#             return self.get_rank()
#
#
# def main():
#     n = int(input('Please! Enter the number of cards to be generated randomly: '))
#     for i in range(n):
#         rank = randint(1, 13)
#         suit = choice(['s', 'd', 'c', 'h'])
#         card = PlayingCard(rank, suit)
#         print(card)
#
#
# main()
#
# # 12.
# from graphics import *
# from random import randint, choice
#
# class Button:
#     """A button is a labeled rectangle in a window .
#     It is activated or deactivated with the activate()
#     and deactivate() methods. The clicked (p) method
#     returns true if the button is active and p is inside it."""
#
#     def __init__(self, win, center, width, height, label):
#         """ Creates a rectangular button, eg:
#         qb = Button(my_win, center_point, width, height, 'Quit') """
#
#         w, h = width / 2.0, height / 2.0
#         x, y = center.getX(), center.getY()
#         self.x_max, self.x_min = x + w, x - w
#         self.y_max, self.y_min = y + h, y - h
#         p1 = Point(self.x_min, self.y_min)
#         p2 = Point(self.x_max, self.y_max)
#         self.rect = Rectangle(p1, p2)
#         self.rect.setFill('lightgray')
#         self.rect.draw(win)
#         self.label = Text(center, label)
#         self.label.draw(win)
#         self.deactivate()
#
#     def clicked(self, p):
#         """ Returns True if button active and p is inside """
#         return self.active and self.x_min <= p.getX() <= self.x_max and self.y_min <= p.getY() <= self.y_max
#
#     def get_label(self):
#         """ Returns the label string of this button. """
#         return self.label.getText()
#
#     def activate(self):
#         """ Sets this button to 'active'. """
#         self.label.setFill('black')
#         self.rect.setWidth(2)
#         self.active = True
#
#     def deactivate(self):
#         """ Sets this button to 'inactive'. """
#         self.label.setFill('darkgrey')
#         self.rect.setWidth(1)
#         self.active = False
#
#
# class PlayingCard:
#
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#
#     def __str__(self):
#         if self.rank == 1:
#             rank_string = 'Ace'
#         elif self.rank == 11:
#             rank_string = 'Jack'
#         elif self.rank == 12:
#             rank_string = 'Queen'
#         elif self.rank == 13:
#             rank_string = 'King'
#         else:
#             rank_string = self.rank
#
#         if self.suit == 's':
#             suit_string = 'Spades'
#         elif self.suit == 'h':
#             suit_string = 'Hearts'
#         elif self.suit == 'c':
#             suit_string = 'Clubs'
#         elif self.suit == 'd':
#             suit_string = 'Diamonds'
#
#         return '{0} of {1}'.format(rank_string, suit_string)
#
#     def get_rank(self):
#         return self.rank
#
#     def get_suit(self):
#         return self.suit
#
#     def value(self):
#         if self.rank > 10:
#             return 10
#         else:
#             return self.get_rank()
#
#
# def main():
#     win = GraphWin('Playing Cards!', 1024, 780)
#     win.setCoords(0, -12, 32, 12)
#
#     draw_button = Button(win, Point(16, -2), 8, 2, 'Draw!')
#     quit_button = Button(win, Point(16, -8), 2, 1, 'Quit')
#
#     draw_button.activate()
#     quit_button.activate()
#
#     while True:
#         pt = win.getMouse()
#
#         if draw_button.clicked(pt):
#
#             cards = []
#             while len(set(cards)) != 5:
#                 rank = randint(1, 13)
#                 suit = choice(['s', 'd', 'c', 'h'])
#                 card = PlayingCard(rank, suit)
#                 cards.append(card)
#
#             filenames = ['{0}_resized.png'.format(card.__str__().replace(' ', '_')).lower() for card in cards]
#
#             anchor_points = list(range(8, 25, 4))
#             for idx, anchor_point in enumerate(anchor_points):
#                 im = Image(Point(anchor_point, 5), 'playing_cards/{0}'.format(filenames[idx]))
#                 im.draw(win)
#
#         if quit_button.clicked(pt):
#             return
#
#
# main()
#
# # 13.
# from graphics import *
# from cbutton import CButton
#
# class Face:
#
#     def __init__(self, window, center, size):
#         self.window = window
#         self.center = center
#         self.size = size
#         self.head = Circle(self.center, self.size)
#         self.eye_size = 0.15 * self.size
#         self.eye_off = self.size / 3.0
#         self.mouth_size = 0.8 * self.size
#         self.mouth_off = self.size / 2.0
#         self.left_eye = None
#         self.right_eye = None
#         p1 = self.center.clone()
#         p2 = self.center.clone()
#         p1.move(-self.mouth_size / 2, self.mouth_off)
#         p2.move(self.mouth_size / 2, self.mouth_off)
#         self.left_edge_mouth = p1
#         self.right_edge_mouth = p2
#         self.mouth = None
#
#     def _draw_head(self):
#         self.head.draw(self.window)
#
#     def _open_left_eye(self):
#         self.left_eye = Circle(self.center, self.eye_size)
#         self.left_eye.move(-self.eye_off, -self.eye_off)
#         self.left_eye.draw(self.window)
#
#     def _open_right_eye(self):
#         self.right_eye = Circle(self.center, self.eye_size)
#         self.right_eye.move(self.eye_off, -self.eye_off)
#         self.right_eye.draw(self.window)
#
#     def _draw_flat_mouth(self):
#         self.mouth = Line(self.left_edge_mouth, self.right_edge_mouth)
#         self.mouth.draw(self.window)
#
#     def _draw_smiling_mouth(self):  # TODO
#         # use Polygon
#         left_x, left_y = self.left_edge_mouth.getX(), self.left_edge_mouth.getY()
#         right_x, right_y = self.right_edge_mouth.getX(), self.right_edge_mouth.getY()
#         middle_x = int((left_x + right_x) / 2)
#         middle_y = int((left_y + right_y) / 2)
#         offset = self.size * 0.15
#         points = [Point(left_x, left_y),
#                   Point((left_x + middle_x) / 2, left_y + offset / 2),
#                   Point(middle_x, middle_y + offset * 0.75),
#                   Point((middle_x + right_x) / 2, right_y + offset / 2),
#                   Point(right_x, right_y)]
#         self.mouth = Polygon(points)
#         self.mouth.draw(self.window)
#
#     def _draw_winking_mouth(self):  # TODO
#         left_x, left_y = self.left_edge_mouth.getX(), self.left_edge_mouth.getY()
#         right_x, right_y = self.right_edge_mouth.getX(), self.right_edge_mouth.getY()
#         middle_x = int((left_x + right_x) / 2)
#         middle_y = int((left_y + right_y) / 2)
#         offset = self.size * 0.20
#         points = [Point(left_x, left_y),
#                   Point((left_x + middle_x) / 2, left_y + offset / 2),
#                   Point(middle_x, middle_y + offset * 0.75),
#                   Point((middle_x + right_x) / 2, right_y + offset / 2),
#                   Point(right_x, right_y - offset * 0.6),
#                   Point((middle_x + right_x) / 2, right_y - offset * 0.45),
#                   Point(middle_x, middle_y - offset * 0.2),
#                   Point((left_x + middle_x) / 2, left_y - offset * 0.1)]
#         self.mouth = Polygon(points)
#         self.mouth.draw(self.window)
#
#     def smile(self):
#         self._remove_face()
#         self._draw_head()
#         self._open_left_eye()
#         self._open_right_eye()
#         self._draw_smiling_mouth()
#
#     def _wink_eye(self):
#         if self.right_eye is not None:
#             self.right_eye.undraw()
#             p = self.right_eye.getCenter()
#             x, y = p.getX(), p.getY()
#         else:  # first time drawing the eye
#             p = self.center.clone()
#             p.move(self.eye_off, -self.eye_off)
#             x, y = p.getX(), p.getY()
#
#         self.right_eye = Line(Point(x - self.eye_size, y), Point(x + self.eye_size, y))
#         self.right_eye.draw(self.window)
#
#     def _draw_flinch_eyes(self):
#         if self.left_eye is not None: self.left_eye.undraw()
#         if self.right_eye is not None: self.right_eye.undraw()
#         p1 = self.center.clone()
#         p2 = self.center.clone()
#         p1.move(-self.eye_off, -self.eye_off)
#         p2.move(self.eye_off, -self.eye_off)
#         left_x, left_y = p1.getX(), p1.getY()
#         right_x, right_y = p2.getX(), p2.getY()
#         offset = self.size * 0.05
#         self.left_eye = Line(Point(left_x - self.eye_size, left_y - offset),
#                              Point(left_x + self.eye_size, left_y + offset))
#         self.right_eye = Line(Point(right_x - self.eye_size, right_y + offset),
#                               Point(right_x + self.eye_size, right_y - offset))
#         self.left_eye.draw(self.window)
#         self.right_eye.draw(self.window)
#
#     def wink(self):
#         self._remove_face()
#         self._draw_head()
#         self._open_left_eye()
#         self._wink_eye()
#         self._draw_winking_mouth()
#
#     def flinch(self):
#         self._remove_face()
#         self._draw_head()
#         self._draw_flinch_eyes()
#         self._draw_flat_mouth()
#
#     def _remove_face(self):
#         self.head.undraw()
#         if self.left_eye is not None:
#             self.left_eye.undraw()
#         if self.right_eye is not None:
#             self.right_eye.undraw()
#         if self.mouth is not None:
#             self.mouth.undraw()
#
#
# def main():
#     width = 1024
#     height = 768
#     win = GraphWin('Faces!', width, height)
#     wink_button = CButton(win, Point(60, 60), 45, 'Winky Face')
#     smile_button = CButton(win, Point(60, 210), 45, 'Smiley Face')
#     flinch_button = CButton(win, Point(60, 360), 45, 'Flinch Face')
#     quit_button = CButton(win, Point(width - 50, height / 2), 20, 'Quit')
#
#     wink_button.activate()
#     smile_button.activate()
#     flinch_button.activate()
#     quit_button.activate()
#
#     f1 = Face(win, Point(int(width / 2), int(height / 2)), 150)
#
#     while True:
#         pt = win.getMouse()
#         if quit_button.clicked(pt):
#             return
#         if wink_button.clicked(pt):
#             f1.wink()
#         if smile_button.clicked(pt):
#             f1.smile()
#         if flinch_button.clicked(pt):
#             f1.flinch()
#
#
# main()
#
# # 14.
# from graphics import *
# from cbutton import CButton
# from random import choice
#
# class Face:
#
#     def __init__(self, window_width, window_height, center, size):
#         self.window_width = window_width
#         self.window_height = window_height
#         self.window = GraphWin('Face', self.window_width, self.window_height)
#         self.center = center
#         self.size = size
#         self.head = None
#         self.eye_size = 0.15 * self.size
#         self.eye_off = self.size / 3.0
#         self.mouth_size = 0.8 * self.size
#         self.mouth_off = self.size / 2.0
#         self.left_eye = None
#         self.right_eye = None
#         self.mouth = None
#
#     def _draw_head(self):
#         if self.head is None:
#             self.head = Circle(self.center, self.size)
#         else:
#             center = self.head.getCenter()
#             self.head = Circle(center, self.size)
#         self.head.draw(self.window)
#         p1 = self.head.getCenter().clone()
#         p2 = self.head.getCenter().clone()
#         p1.move(-self.mouth_size / 2, self.mouth_off)
#         p2.move(self.mouth_size / 2, self.mouth_off)
#         self.left_edge_mouth = p1
#         self.right_edge_mouth = p2
#
#     def _open_left_eye(self):
#         self.left_eye = Circle(self.head.getCenter(), self.eye_size)
#         self.left_eye.move(-self.eye_off, -self.eye_off)
#         self.left_eye.draw(self.window)
#
#     def _open_right_eye(self):
#         self.right_eye = Circle(self.head.getCenter(), self.eye_size)
#         self.right_eye.move(self.eye_off, -self.eye_off)
#         self.right_eye.draw(self.window)
#
#     def _draw_flat_mouth(self):
#         self.mouth = Line(self.left_edge_mouth, self.right_edge_mouth)
#         self.mouth.draw(self.window)
#
#     def _draw_smiling_mouth(self):
#         left_x, left_y = self.left_edge_mouth.getX(), self.left_edge_mouth.getY()
#         right_x, right_y = self.right_edge_mouth.getX(), self.right_edge_mouth.getY()
#         middle_x = int((left_x + right_x) / 2)
#         middle_y = int((left_y + right_y) / 2)
#         offset = self.size * 0.15
#         points = [Point(left_x, left_y),
#                   Point((left_x + middle_x) / 2, left_y + offset / 2),
#                   Point(middle_x, middle_y + offset * 0.75),
#                   Point((middle_x + right_x) / 2, right_y + offset / 2),
#                   Point(right_x, right_y)]
#         self.mouth = Polygon(points)
#         self.mouth.draw(self.window)
#
#     def _draw_winking_mouth(self):
#         left_x, left_y = self.left_edge_mouth.getX(), self.left_edge_mouth.getY()
#         right_x, right_y = self.right_edge_mouth.getX(), self.right_edge_mouth.getY()
#         middle_x = int((left_x + right_x) / 2)
#         middle_y = int((left_y + right_y) / 2)
#         offset = self.size * 0.20
#         points = [Point(left_x, left_y),
#                   Point((left_x + middle_x) / 2, left_y + offset / 2),
#                   Point(middle_x, middle_y + offset * 0.75),
#                   Point((middle_x + right_x) / 2, right_y + offset / 2),
#                   Point(right_x, right_y - offset * 0.6),
#                   Point((middle_x + right_x) / 2, right_y - offset * 0.45),
#                   Point(middle_x, middle_y - offset * 0.2),
#                   Point((left_x + middle_x) / 2, left_y - offset * 0.1)]
#         self.mouth = Polygon(points)
#         self.mouth.draw(self.window)
#
#     def _remove_face(self):
#         if self.head is not None:
#             self.head.undraw()
#         if self.left_eye is not None:
#             self.left_eye.undraw()
#         if self.right_eye is not None:
#             self.right_eye.undraw()
#         if self.mouth is not None:
#             self.mouth.undraw()
#
#     def _wink_eye(self):
#         if self.right_eye is not None:
#             self.right_eye.undraw()
#             p = self.right_eye.getCenter()
#             x, y = p.getX(), p.getY()
#         else:  # first time drawing the eye
#             p = self.center.clone()
#             p.move(self.eye_off, -self.eye_off)
#             x, y = p.getX(), p.getY()
#
#         self.right_eye = Line(Point(x - self.eye_size, y), Point(x + self.eye_size, y))
#         self.right_eye.draw(self.window)
#
#     def _draw_flinch_eyes(self):
#         if self.left_eye is not None: self.left_eye.undraw()
#         if self.right_eye is not None: self.right_eye.undraw()
#         p1 = self.head.getCenter().clone()
#         p2 = self.head.getCenter().clone()
#         p1.move(-self.eye_off, -self.eye_off)
#         p2.move(self.eye_off, -self.eye_off)
#         left_x, left_y = p1.getX(), p1.getY()
#         right_x, right_y = p2.getX(), p2.getY()
#         offset = self.size * 0.05
#         self.left_eye = Line(Point(left_x - self.eye_size, left_y - offset),
#                              Point(left_x + self.eye_size, left_y + offset))
#         self.right_eye = Line(Point(right_x - self.eye_size, right_y + offset),
#                               Point(right_x + self.eye_size, right_y - offset))
#         self.left_eye.draw(self.window)
#         self.right_eye.draw(self.window)
#
#     def _get_x_y(self):
#         p = self.head.getCenter()
#         x = p.getX()
#         y = p.getY()
#         return x, y
#
#     def _beyond_right(self):
#         x, y = self._get_x_y()
#         return x + self.size > self.window_width
#
#     def _beyond_bottom(self):
#         x, y = self._get_x_y()
#         return y + self.size > self.window_height
#
#     def _away_left(self):
#         x, y = self._get_x_y()
#         return x - self.size < 0
#
#     def _away_up(self):
#         x, y = self._get_x_y()
#         return y - self.size < 0
#
#     def _is_on_edge(self):
#         x, y = self._get_x_y()
#         if not self._beyond_right() and not self._away_up() and not self._beyond_bottom() and not self._away_left():
#             return False
#         return True
#
#     def _move(self, dx, dy):
#         self.head.move(dx, dy)
#         self.left_eye.move(dx, dy)
#         self.right_eye.move(dx, dy)
#         self.mouth.move(dx, dy)
#
#     def wink(self):
#         self._remove_face()
#         self._draw_head()
#         self._open_left_eye()
#         self._wink_eye()
#         self._draw_winking_mouth()
#
#     def flinch(self):
#         self._remove_face()
#         self._draw_head()
#         self._draw_flinch_eyes()
#         self._draw_flat_mouth()
#
#     def smile(self):
#         self._remove_face()
#         self._draw_head()
#         self._open_left_eye()
#         self._open_right_eye()
#         self._draw_smiling_mouth()
#
#     def move(self):
#         dx = 1
#         dy = 1
#         for i in range(10000):
#             if not self._is_on_edge():
#                 self._move(dx, dy)
#             else:
#                 if self._beyond_right():
#                     dx = -1
#                 elif self._away_up():
#                     dy = 1
#                 elif self._beyond_bottom():
#                     dy = -1
#                 elif self._away_left():
#                     dx = 1
#
#                 self._remove_face()
#                 face_type = choice(['wink', 'smile', 'flinch'])
#                 if face_type == 'wink':
#                     self.wink()
#                 elif face_type == 'smile':
#                     self.smile()
#                 else:
#                     self.flinch()
#                 self._move(dx, dy)
#             update(100)
#
#
# def main():
#     width = 1024
#     height = 768
#
#     f1 = Face(width, height, Point(int(width / 2), int(height / 2)), 150)
#     f1.smile()
#     f1.move()
#
#
# main()

# 15.
from graphics import *
from cannonball import ShotTracker, InputDialog

def main():

    # create animation window
    win = GraphWin('Projectile Animation', 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)

    # draw baseline
    Line(Point(-10, 0), Point(210, 0)).draw(win)

    # draw labeled ticks every 50 meters
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)

    # event loop, each time through fires a single shot
    angle, vel, height = 45.0, 40.0, 2.0
    input_win = InputDialog(angle, vel, height)
    while True:
        # interact with the user
        choice = input_win.interact()

        if choice == 'Quit': # loop exit
            break

        # create a shot and track until it hits ground or leaves window
        angle, vel, height = input_win.get_values()
        shot = ShotTracker(win, angle, vel, height)
        while 0 <= shot.get_y() and -10 < shot.get_x() <= 210:
            shot.update(1/50)
            update(50)

    win.close()


main()

# 16.
