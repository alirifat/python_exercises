# Exercise 1.4

total_seconds = 43 * 60 + 30
seconds_in_minute = 60 * 60
length_in_mile = 10 / 1.61

print("Average time per mile: ", end='')
print('{} min/mile'.format(round(((total_seconds / length_in_mile) / 60), 2)))

average_speed = (seconds_in_minute * length_in_mile) / total_seconds
print('\nAverage speed in miles per hour: ', end='')
print('{} mile/hour'.format(round(average_speed, 2)))
