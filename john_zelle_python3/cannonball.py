from graphics import *
from math import radians, cos, sin

class Button:
    """A button is a labeled rectangle in a window .
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked (p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(my_win, center_point, width, height, 'Quit') """

        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.x_max, self.x_min = x + w, x - w
        self.y_max, self.y_min = y + h, y - h
        p1 = Point(self.x_min, self.y_min)
        p2 = Point(self.x_max, self.y_max)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """ Returns True if button active and p is inside """
        return self.active and self.x_min <= p.getX() <= self.x_max and self.y_min <= p.getY() <= self.y_max

    def get_label(self):
        """ Returns the label string of this button. """
        return self.label.getText()

    def activate(self):
        """ Sets this button to 'active'. """
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """ Sets this button to 'inactive'. """
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False


class Projectile:
    """ Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x). """

    def __init__(self, angle, velocity, height):
        """ Create a projectile with given launch angle, initial
        velocity and height. """
        self.x_pos = 0.0
        self.y_pos = height
        theta = radians(angle)
        self.x_vel = velocity * cos(theta)
        self.y_vel = velocity * sin(theta)

    def update(self, time):
        """ Update the state of this projectile to move it time seconds
        farther into its flight. """
        self.x_pos = self.x_pos + time * self.x_vel
        y_vel1 = self.y_vel - 9.8 * time
        self.y_pos = self.y_pos + time * (self.y_vel + y_vel1) / 2.0
        self.y_vel = y_vel1

    def get_y(self):
        """" Returns the y position (height) of this projectile. """
        return self.y_pos

    def get_x(self):
        """ Returns the x position (distance) of this projectile. """
        return self.x_pos


class ShotTracker:

    def __init__(self, win, angle, velocity, height):
        """ win is the GraphWin to display the shot. angle, velocity,
        and height are initial projectile parameters."""

        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill('red')
        self.marker.setOutline('red')
        self.marker.draw(win)

    def update(self, dt):
        """ Move the shot dt seconds farther along its flight. """

        # update the projectile
        self.proj.update(dt)

        # move the circle to the new projectile location
        center = self.marker.getCenter()
        dx = self.proj.get_x() - center.getX()
        dy = self.proj.get_y() - center.getY()
        self.marker.move(dx, dy)

    def get_x(self):
        """ Return the current x coordinate of the shot's center """
        return self.proj.get_x()

    def get_y(self):
        """ Return the current y coordinate of the shot's center """
        return self.proj.get_y()

    def undraw(self):
        """ Undraw the shot. """
        self.marker.undraw()


class InputDialog:
    """ A custom window for getting simulation values (angle, velocity,
    and height) from the user. """

    def __init__(self, angle, vel, height):
        """ Build and display the input window. """

        self.win = win = GraphWin('Initial Values', 200, 300)
        win.setCoords(0, 4.5, 4, 0.5)

        Text(Point(1, 1), 'Angle').draw(win)
        self.angle = Entry(Point(3, 1), 5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1, 2), 'Velocity').draw(win)
        self.vel = Entry(Point(3, 2), 5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1, 3), 'Height').draw(win)
        self.height = Entry(Point(3, 3), 5).draw(win)
        self.height.setText(str(height))

        self.fire = Button(win, Point(1, 4), 1.25, 0.5, 'Fire!')
        self.fire.activate()

        self.quit = Button(win, Point(3, 4), 1.25, 0.5, 'Quit')
        self.quit.activate()

    def interact(self):
        """ Wait for user to click Quit or Fire buttons.
        Returns a string indicating which button was clicked. """

        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return 'Quit'
            if self.fire.clicked(pt):
                return 'Fire!'

    def get_values(self):
        """ Return input values. """

        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())
        return a, v, h


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
    while True:
        # interact with the user
        input_win = InputDialog(angle, vel, height)
        choice = input_win.interact()
        input_win.win.close()

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