def has_no_e(s):
    return not 'e' in s

def words_no_e(words):
    count = 0
    for word in words:
        if has_no_e(word):
            count += 1
    return count

file = '/Users/Ali R Kaya/Desktop/words.txt'
with open(file, 'r') as fin:
    words = fin.readlines()

word_without_e = words_no_e(words)
print(100 * (word_without_e / len(words)))
