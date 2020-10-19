def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

def reverse_lookup(d, v):
    keys = []
    for k in d:
        if d[k] == v:
            keys.append(k)
    return keys

h = histogram('brontosaurus')
print(reverse_lookup(h, 1))
print(reverse_lookup(h, 10))
