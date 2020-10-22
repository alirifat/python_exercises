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

print(tokenize_v1('jane_austen.txt'))

def tokenize_v2(file):
    t = tokenize_v1(file)
    print('Total number of words:', len(t))
    histogram = dict()
    for word in t:
        histogram[word] = histogram.get(word, 0) + 1
    print('Number of unique words:', len(histogram.keys()))
    return histogram

print('Jane Austen')
tokenize_v2('jane_austen.txt')

print('\nPlato')
tokenize_v2('plato.txt')

print('\nPercy Neville')
tokenize_v2('percy_neville.txt')
