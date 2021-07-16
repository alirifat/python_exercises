from graphics import *


class CButton:
    """A button is a labeled rectangle in a window .
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked (p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, radius, label):
        """ Creates a rectangular button, eg:
        qb = Button(my_win, center_point, width, height, 'Quit') """

        self.radius = radius
        self.center = center
        self.circle = Circle(center, radius)
        self.circle.setFill('lightgray')
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """ Returns True if button active and p is inside """
        distance = self._get_distance(p)
        return self.active and distance <= self.radius

    def get_label(self):
        """ Returns the label string of this button. """
        return self.label.getText()

    def activate(self):
        """ Sets this button to 'active'. """
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        """ Sets this button to 'inactive'. """
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False

    def _get_distance(self, p):
        return (abs(p.getX() - self.center.getX()) ** 2 + abs(p.getY() - self.center.getY()) ** 2) ** (1 / 2)
