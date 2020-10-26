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

def mul_time(time, number):
    in_seconds = time_to_int(time)
    res = in_seconds * number
    return int_to_time(res)

class Time():
    '''Attributes hour, minute, second'''

time = Time()
time.hour = 9
time.minute = 37
time.seconds = 22

res = mul_time(time, 6785)
print(('{}'.format(res.hour).zfill(2)+':'+\
       '{}'.format(res.minute).zfill(2)+':'+\
       '{}'.format(res.seconds).zfill(2)))

finish_time = Time()
finish_time.hour, finish_time.minute, finish_time.seconds = 0, 45, 17
distance = 11.5

average_pace = mul_time(finish_time, 1/distance)
print(('{}'.format(int(average_pace.hour)).zfill(2)+':'+\
       '{}'.format(int(average_pace.minute)).zfill(2)+':'+\
       '{}'.format(int(average_pace.seconds)).zfill(2)))
