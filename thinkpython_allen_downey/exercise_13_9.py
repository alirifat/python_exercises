from string import whitespace, punctuation
from math import log

def skip_header(text):
    for line in text:
        if line.strip(punctuation+whitespace).lower().startswith('start of'):
            break

def zip_law(file):
    words = {}
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
        for w in word: words[w] = words.get(w, 0) + 1
    words = [(v, k) for k, v in words.items()]
    words.sort(reverse=True)
    print('frequency', 'word', 'log_f', 'log_r')
    for idx, (freq, word) in enumerate(words):
        print(freq, word, log(freq), log(idx+1))
    return words

zip_law('emma.txt')
