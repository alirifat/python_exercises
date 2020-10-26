class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.seconds = hour * 3600 + minute * 60 + second

    def int_to_time(self):
        """Makes a new Time object.
        seconds: int seconds since midnight.
        """
        minutes, second = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        hour %= 24
        return hour, minute, second

    def __str__(self):
        """Returns a string representation of the time."""
        time = self.int_to_time()
        return '{}'.format(time[0]).zfill(2)+':'+\
               '{}'.format(time[1]).zfill(2)+':'+\
               '{}'.format(time[2]).zfill(2)

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.seconds > other.seconds

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.
        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        time = self.seconds + other.seconds
        return int_to_time(time)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        time = self.seconds + seconds
        return int_to_time(time)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.seconds >= 0:
            return True
        else:
            return True

def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()
