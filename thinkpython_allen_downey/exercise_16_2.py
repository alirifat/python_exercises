def get_time(Time):
    return ('{}'.format(Time.hour).zfill(2)+':'+\
          '{}'.format(Time.minute).zfill(2)+':'+\
          '{}'.format(Time.second).zfill(2))

def is_after(time1, time2):
    return get_time(time1) < get_time(time2)

class Time():
    '''Attributes hour, minute, second'''

time1 = Time()
time1.hour = 9
time1.minute = 37
time1.second = 22

time2 = Time()
time2.hour = 9
time2.minute = 37
time2.second = 23

print(is_after(time1, time2))
