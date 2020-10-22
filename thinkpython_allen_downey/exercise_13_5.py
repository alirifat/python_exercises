import random

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

def chose_from_hist(hist):
    choice = random.choices(list(hist.keys()), weights=list(hist.values()))
    return choice

h = histogram('brontosaurus')
print(chose_from_hist(h))
