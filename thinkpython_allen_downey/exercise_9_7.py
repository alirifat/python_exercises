def find_double_consequtive(file):
    with open(file, 'r') as fin:
        words = fin.readlines()
    for word in words:
        i = 0
        count = 0
        while i < len(word) - 1:
            if word[i] == word[i+1]:
                count += 1
                if count == 3:
                    return word
                i += 2
            else:
                count = 0
                i += 1

print(find_double_consequtive('/Users/Ali R Kaya/Desktop/words.txt'))

# Another solution may be counting the characters of the words
def find_double_consequtive(file):
    with open(file, 'r') as fin:
        words = fin.readlines()
    for word in words:
        for i in range(len(word)):
            if i < len(word) - 5:
                first_double = word[i] == word[i+1]
                second_double = word[i+2] == word[i+3]
                third_double = word[i+4] == word[i+5]
                if first_double and second_double and third_double:
                    return word

print(find_double_consequtive('/Users/Ali R Kaya/Desktop/words.txt'))
