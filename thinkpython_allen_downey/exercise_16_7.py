### Part 1
def day_of_the_week():
    import datetime
    now = datetime.datetime.now()
    day = now.weekday()
    days = dict(zip([i for i in range(7)],
                    ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday',
                     'Sunday']))
    return days[day]

print(day_of_the_week())

### Part 2

def countdown_birhtday():
    from datetime import date, datetime
    bd = input('Please enter your birthday (YYYY-MM-DD):')
    bd_year, bd_month, bd_day = (int(i) for i in bd.split('-'))
    today = datetime.today()
    diff = datetime(today.year, bd_month, bd_day) - today
    if diff.days < 0 : return (-1) * diff.days
    else: return diff.days

print(countdown_birhtday())


### Part 3

def find_double_day():
    from datetime import datetime
    b1 = input('Please enter the first birthday (YYYY-MM-DD):')
    b2 = input('Please enter the second birhtday (YYYY-MM-DD):')
    b1_year, b1_month, b1_day = (int(i) for i in b1.split('-'))
    b2_year, b2_month, b2_day = (int(i) for i in b2.split('-'))
    b1 = datetime(b1_year, b1_month, b1_day)
    b2 = datetime(b2_year, b2_month, b2_day)
    diff = b1 - b2
    if diff.days < 0:
        b1 + (-1)*diff
        return b1
    else: return b1 + diff

print(find_double_day())

### Part 4

def find_double_day(n):
    from datetime import datetime
    b1 = input('Please enter the first birthday (YYYY-MM-DD):')
    b2 = input('Please enter the second birhtday (YYYY-MM-DD):')
    b1_year, b1_month, b1_day = (int(i) for i in b1.split('-'))
    b2_year, b2_month, b2_day = (int(i) for i in b2.split('-'))
    b1 = datetime(b1_year, b1_month, b1_day)
    b2 = datetime(b2_year, b2_month, b2_day)
    diff = b1 - b2
    if diff.days < 0:
        b1 + (-1)*(n-1)*diff
        return b1
    else: return b1 + (n-1)*diff

print(find_double_day(5))
