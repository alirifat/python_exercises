# Part 1
from string import whitespace, punctuation
import random

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

tokens = tokenize_v1('emma.txt')

def markov_analysis(tokens, order=2):
    markov = {}
    i = 0
    j = order
    while i < len(tokens) - j:
        prefix = tokens[i:i+j]
        suffix = tokens[i+j]
        key = tuple(prefix)
        if key not in markov:
            markov[key] = [suffix]
        else:
            markov[key].append(suffix)
        i += 1
    return markov

print(markov_analysis(tokens, 2))

# Part 2
markov = markov_analysis(tokens, 2)

def random_text_generator(markov, length=50):
    start = random.choice(list(markov.keys()))
    for i in range(length):
        try:
            suffixes = markov[start]
        except KeyError:
            random_text_generator(markov, length-i)
            return
        suffix = random.choice(suffixes)
        print(suffix, end=' ')
        start = tuple([start[1] + suffix])

random_text_generator(markov, 50)
