def uses_all(word, letters):
    for letter in letters:
        if not letter in word:
            return False
    return True

print(uses_all('laptop', 'lpt'))

# find the number of words uses all vowels
def find_all(file, letters='aeiou'):
    with open(file, 'r') as fin:
        words = fin.readlines()
    count = 0
    for word in words:
        inner_count = 0
        for letter in letters:
            if letter in word:
                inner_count += 1
        if inner_count == len(letters):
            count += 1
    return count

print(find_all('words.txt'))
print(find_all('words.txt', 'aeiouy'))
