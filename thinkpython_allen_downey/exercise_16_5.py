def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.seconds
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.seconds = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    time.hour %= 24
    return time

def increment(time, seconds):
    in_seconds = time_to_int(time)
    res = in_seconds + seconds
    return int_to_time(res)

class Time():
    """Attributes hour, minute, seconds"""

time = Time()
time.hour, time.minute, time.seconds = 9, 37, 22

res = increment(time, 100)
print(('{}'.format(res.hour).zfill(2)+':'+\
       '{}'.format(res.minute).zfill(2)+':'+\
       '{}'.format(res.seconds).zfill(2)))
