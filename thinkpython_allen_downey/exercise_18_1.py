class Time():
    '''Attributes hour, minute, second'''
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __lt__(self, other):
        t1 = (self.hour, self.minute, self.second)
        t2 = (other.hour, other.minute, other.second)
        return t1 < t2


t1 = Time(9, 15, 52)
t2 = Time(9, 15, 51)

print(t1 > t2)
