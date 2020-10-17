def has_duplicates(t):
    index = 0
    while index < len(t):
        if t[index] in t[index+1:]:
            return True
        index += 1
    return False

print(has_duplicates(['a','b','c','a']))

def birhtday_pradox(number_of_birhtdays, number_of_times):
    from random import randint
    duplicates = 0
    for i in range(number_of_times):
        birthdays = []
        for i in range(number_of_birhtdays):
            birthdays.append(randint(1,365))
        if has_duplicates(birthdays):
            duplicates += 1
    return (duplicates / number_of_times) * 100

print(birhtday_pradox(23, 1000))
