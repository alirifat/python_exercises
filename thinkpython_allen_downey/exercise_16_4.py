class Time():
    '''Attributes hour, minute, second'''

def increment(time, seconds):
    res = Time()
    minute, second = divmod((time.seconds + seconds), 60)
    res.seconds = second
    res.minute = time.minute + minute
    res.hour = time.hour
    return ('{}'.format(res.hour).zfill(2)+':'+\
            '{}'.format(res.minute).zfill(2)+':'+\
            '{}'.format(res.seconds).zfill(2))

time = Time()
time.hour = 9
time.minute = 37
time.seconds = 22

print(increment(time, 59))
