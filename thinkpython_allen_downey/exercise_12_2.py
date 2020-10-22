with open('words.txt', 'r') as fin:
    lines = fin.readlines()
words = []
for line in lines:
    words.append(line.strip())

def unstable_sort(words):
    import random
    t = []
    for word in words:
        t.append((len(word), random.random(), word))
    t.sort(reverse=True)
    res = []
    for length, r, word in t:
        res.append(word)
    return res

print(unstable_sort[:10])
