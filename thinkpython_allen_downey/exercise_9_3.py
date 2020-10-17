def avoids(word, letters):
    for letter in letters:
        if letter in word:
            return False
    return True

print(avoids('avoids', 'xyz'))

# checks how many of the words do not contain any of the forbidden letters
def avoids_input(file):
    with open(file, 'r') as fin:
        words = fin.readlines()
    forbidden_letters = input('Please enter a series of letters:')
    count = 0
    for word in words:
        letters = 0
        for letter in forbidden_letters:
            if not letter in word:
                letters += 1
            if letters == len(forbidden_letters):
                count += 1
    return count

avoids_input('words.txt')

# find the 5 forbidden letters that excludes the least number of words
def avoids_least(file, letter):
    with open(file, 'r') as fin:
        words = fin.readlines()
    count = 0
    for word in words:
        if not letter in word:
            count += 1
    return count

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    print(letter, avoids_least('words.txt', letter))

# output
# a 57196
# b 97504
# c 83343
# d 83161
# e 37641
# f 102532
# g 88830
# h 94713
# i 53495
# j 112062
# k 104831
# l 73676
# m 91335
# n 64127
# o 69152
# p 90840
# q 112177
# r 58908
# s 49006
# t 66530
# u 84934
# v 104917
# w 105541
# x 111118
# y 100668
# z 110358

# if we were covered 'List' chapter it would be much easier. However, I prefer
# to go with the book so that this process will be manually done.
# the 5 forbidden letters that excludes the least number of words:
# e 37641
# s 49006
# i 53495
# a 57196
# r 58908
# It is 'aeisr' which excludes 58908 words in the list.
