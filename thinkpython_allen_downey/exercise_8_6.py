def find(word, letter, start=0):
    index = start
    while index < len(word):
        if word[index] ==letter:
            return index
        index = index + 1
    return -1

def count(s, letter):
    count = 0
    index = find(s, letter)
    while index > -1:
        count += 1
        index = find(s, letter, index + 1)
    return count

print(count('bookkeeper', 'e'))
