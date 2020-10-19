def read_dictionary(file):
    with open(file, 'r') as fin:
        lines = fin.readlines()
    dictionary = {}
    for line in lines:
        if line[0] in '!"#%&\'()+,-./3:?{};':
            continue
        else:
            word = line.strip().split(' ')
            pronounce = ' '.join(word[1:])
            dictionary[word[0].lower()] = pronounce.replace('0', 'O')
    return dictionary

def read_words(file):
    with open(file, 'r') as fin:
        lines = fin.readlines()
    words = []
    for line in lines:
        words.append(line.strip())

def homophone(word1, word2, dictionary):
    if (word1 in dictionary) and (word2 in dictionary):
        return dictionary[word1] == dictionary[word2]
    return False

def find_words(words, dictionary):
    results = []
    for word in words:
        if len(word) == 5:
            first_condition = word[1:]
            second_condition = word[0] + word[2:]
            if homophone(first_condition, second_condition, dictionary):
                results.append(word)
    return results

dictionary = read_dictionary('dictionary.txt')
words = read_words('words.txt')

print(find_words(words, dictionary))
