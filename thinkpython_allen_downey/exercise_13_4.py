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
        word = line.strip().split()
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
not_in_words = []
for word in hist:
    if word not in words:
        not_in_words.append(word)
print(not_in_words)
