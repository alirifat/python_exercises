def tokenize(file):
    from string import whitespace, punctuation
    words = []
    for line in open(file):
        word = line.strip().split()
        word = [''.join([c.lower() for c in w
                                       if c not in whitespace and
                                           c not in punctuation])
                    for w in word]
        for w in word: words.append(w)
    return words

print(tokenize('jane_austen.txt'))
