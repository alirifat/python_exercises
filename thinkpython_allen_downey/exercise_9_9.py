def check_ages(i, j):
    return str(i).zfill(2) == str(j)[::-1]

def find_difference():
    for diff in range(10, 30):
        son = 0
        count = 0
        while son < 80:
            mother = son + diff
            if check_ages(son, mother):
                count += 1
            son += 1
        if count == 8:
            return diff

diff = find_difference()

def find_son_age(diff):
    count = 0
    for son in range(80):
        mother = son + diff
        if check_ages(son, mother):
            print(son, mother)
            count += 1

find_son_age(diff)
