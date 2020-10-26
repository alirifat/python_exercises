class Time():
    def print_time(self):
        print('{}'.format(self.hour).zfill(2)+':'+\
              '{}'.format(self.minute).zfill(2)+':'+\
              '{}'.format(self.seconds).zfill(2))
    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.seconds
        return seconds

time = Time()
time.hour = 9
time.minute = 37
time.seconds = 22

time.print_time()
print(time.time_to_int())
