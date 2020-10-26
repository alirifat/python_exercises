def increment(Time, seconds):
    minute, second = divmod((Time.seconds + seconds), 60)
    Time.seconds = second
    Time.minute += minute
    return ('{}'.format(Time.hour).zfill(2)+':'+\
            '{}'.format(Time.minute).zfill(2)+':'+\
            '{}'.format(Time.seconds).zfill(2))

class Time():
    '''Attributes hour, minute, second'''

time = Time()
time.hour = 9
time.minute = 37
time.seconds = 22

print(increment(time, 59))
