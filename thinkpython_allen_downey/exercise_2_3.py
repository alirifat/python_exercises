# Part 1
def find_volume(r):
    """Returns the volume of a sphere with a given radius
    """
    from math import pi

    return (4/3)*pi*(r**3)

print(find_volume(5))

# Part 2
cover_price = 24.75
discount = 0.40

def shipping_cost(num_copy):
    """Finds total shipping cost for a given number of copies
    """
    return 3 + 0.75 * (num_copy - 1)

def total_cost(num_books, price, discount):
    """Finds the wholesale cost for a given number of books with given
    discout rate
    """

    return (price*(1-discount))*num_books + shipping_cost(60)

print(f'\nTotal cost: {total_cost(60, cover_price, discount)}')

# Part 3
from math import floor

easy_pace = 8 * 60 + 15
tempo = 7 * 60 + 12

total_run_time = 2 * easy_pace + 3 * tempo
run_minutes = total_run_time // 60
run_hours = floor(total_run_time / (60 * 60))
time_home_minutes = (52 + run_minutes) % 60

time_home_hours = (6 + run_hours) + floor((52 + run_minutes) / 60)
print(f'\nTime at home is {time_home_hours}:{time_home_minutes} am')
