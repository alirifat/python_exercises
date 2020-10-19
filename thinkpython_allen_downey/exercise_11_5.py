def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

def invert_dict(d):
    inverse = dict()
    for key in d:
        value = d[key]
        inverse.setdefault(value, [])
        inverse[value].append(key)
    return inverse

h = histogram('brontosaurus')
print(invert_dict(h))
