def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

h = histogram('brontosaurus')
print(h)
