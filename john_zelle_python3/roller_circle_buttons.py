from random import randrange
from graphics import *
from cbutton import CButton

class DieView:
    """ DieView is a widget that displays a graphical representation of a standard six-sided die. """

    def __init__(self, win, center, size):
        """ Create a view of a die, e.g."
        d1 = DieView(my_win, Point(40, 50), 20)
        creates a die centered at (40, 50) having sides
        of length 20. """

        # first define some standard values
        self.win = win  # save this for drawing pips later
        self.background = 'white'  # color of die face
        self.foreground = 'black'  # color of the pips
        self.p_size = 0.1 * size  # radius of each pip
        h_size = size / 2.0  # half the size of the die
        offset = 0.6 * h_size  # distance from center to outer pips

        # create a square for the face
        c_x, c_y = center.getX(), center.getY()
        p1 = Point(c_x - h_size, c_y - h_size)
        p2 = Point(c_x + h_size, c_y + h_size)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # create 7 circles for standard pip locations
        self.pip1 = self.__make_pip(c_x - offset, c_y - offset)
        self.pip2 = self.__make_pip(c_x - offset, c_y)
        self.pip3 = self.__make_pip(c_x - offset, c_y + offset)
        self.pip4 = self.__make_pip(c_x, c_y)
        self.pip5 = self.__make_pip(c_x + offset, c_y - offset)
        self.pip6 = self.__make_pip(c_x + offset, c_y)
        self.pip7 = self.__make_pip(c_x + offset, c_y + offset)

        # draw an initial value
        self.set_value(1)

    def __make_pip(self, x, y):
        """ Internal helper method to draw a pip at (x, y). """
        pip = Circle(Point(x, y), self.p_size)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def set_value(self, value):
        """ Set this die to display value. """
        # turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        # turn correct pips on
        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)


def main():
    # create the application window
    win = GraphWin('Dice Roller')
    win.setCoords(0, 0, 10, 10)
    win.setBackground('green2')

    # draw the interface widgets
    die1 = DieView(win, Point(3, 8), 2)
    die2 = DieView(win, Point(7, 8), 2)
    roll_button = CButton(win, Point(5, 4.5), 2, 'Roll Dice')
    roll_button.activate()
    quit_button = CButton(win, Point(5, 1), 1, 'Quit')

    # Event loop
    pt = win.getMouse()
    while not quit_button.clicked(pt):
        if roll_button.clicked(pt):
            value1 = randrange(1, 7)
            die1.set_value(value1)
            value2 = randrange(1, 7)
            die2.set_value(value2)
            quit_button.activate()
        pt = win.getMouse()

    # close up shop
    win.close()


main()
