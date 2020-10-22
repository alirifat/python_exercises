from string import whitespace, punctuation

def skip_header(text):
    for line in text:
        if line.strip(punctuation+whitespace).lower().startswith('start of'):
            break

def tokenize_v1(file):
    words = []
    text = open(file, encoding='utf-8')
    skip_header(text)
    for line in text:
        if line.strip(punctuation+whitespace).lower().startswith('end of'):
            break
        word = line.replace('-', ' ').replace('—', ' ')
        word = word.strip().split()
        word = [''.join([c.lower() for c in w
                                       if c not in whitespace and
                                           c not in punctuation+'“”'+"‘’"])
                    for w in word]
        for w in word: words.append(w)
    return words

def tokenize_v2(file):
    t = tokenize_v1(file)
    print('Total number of words:', len(t))
    histogram = dict()
    for word in t:
        histogram[word] = histogram.get(word, 0) + 1
    print('Number of unique words:', len(histogram.keys()))
    return histogram

with open('words.txt') as fin:
    lines = fin.readlines()
words = {k.strip():None for k in lines}

hist = tokenize_v2('jane_austen.txt')

import random
import bisect

def random_word(h):
    words_in_book = []
    freq = []
    for k, v in h.items():
        words_in_book.append(k)
        freq.append(v)
    cumsum = [sum(freq[:i]) for i in range(len(freq))]
    random_number = random.randint(1, freq[-1])
    index = bisect.bisect(cumsum, random_number)
    return words_in_book[index]

print(random_word(hist))
