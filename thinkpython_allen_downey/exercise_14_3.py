with open('words.txt', 'r') as fin:
    lines = fin.readlines()
words = [line.strip() for line in lines]

def anagrams(words):
    d = dict()
    for word in words:
        t = list(word)
        t.sort()
        s = ''.join(t)
        if s not in d:
            d[s] = [word]
        else:
            d[s].append(word)
    return d

d = anagrams(words)

def store_anagrams(filename, d):
    import shelve
    with shelve.open(filename, 'c') as db:
        for key, value in d.items():
            db[key] = value

def read_anagrams(word, database):
    import shelve
    try:
        with shelve.open(database) as db:
            return db['aa']
    except:
        return 'The word does not exist in the database'

store_anagrams('anagrams_db', d)
read_anagrams('aa', 'anagrams_db')
