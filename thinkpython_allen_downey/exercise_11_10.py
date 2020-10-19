def rotate_word(string, integer):
    rotated = ''
    for char in string:
        num = ord(char)
        if (num > 64) and (num < 91):
            new = ((num + (integer % 26)) % 91) % 65
            rotated += chr(65 + new)
        if (num > 96) and (num < 123):
            new = ((num + (integer % 26)) % 123) % 97
            rotated += chr(97 + new)
    return rotated

def find_rotated_words(words_d, range_):
    for i in range(1, range_):
        for key in words_d:
            rotated = rotate_word(key, i)
            if rotated in words_d:
                words_d[key].append(rotated)
    return words_d

with open('words.txt', 'r') as fin:
    lines = fin.readlines()
words_d = dict()
for line in lines:
    words_d[line.strip()] = []

find_rotated_words(words_d, 10)
