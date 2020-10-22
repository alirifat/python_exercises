def read_file(file):
    with open(file, 'r') as fin:
        lines = fin.readlines()
    words = [line.strip() for line in lines if line.strip() != '']
    return words

german_words = read_file('german.txt')
german_words = [s for line in german_words for s in line.split()]
german_words = [''.join([c.lower() for c in word
                             if c not in r'."¼:¤¶;?\'!*_)(-)®`´¢¨©»¦º¹§+„³,1234567890ª'])
                for word in german_words]
french_words = read_file('french.txt')
french_words = [''.join([c.lower() for c in word
                             if c not in '©¢¨®-§ª»¯´¼\xa0«¶¹¤'])\
                for word in french_words]
english_words = read_file('words.txt')

def most_frequent(t):
    d = dict()
    for s in t:
        for c in s.lower():
            d[c] = d.get(c, 0) + 1
    t = [(v, k) for k, v in d.items()]
    t.sort(reverse=True)
    return [word for freq, word in t]

print(most_frequent(german_words))
print(most_frequent(english_words))
print(most_frequent(french_words))
