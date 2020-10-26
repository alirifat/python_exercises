def print_time(Time):
    print('{}'.format(Time.hour).zfill(2)+':'+\
          '{}'.format(Time.minute).zfill(2)+':'+\
          '{}'.format(Time.second).zfill(2))

class Time():
    '''Attributes hour, minute, second'''

time = Time()
time.hour = 9
time.minute = 37
time.second = 22

print_time(time)
