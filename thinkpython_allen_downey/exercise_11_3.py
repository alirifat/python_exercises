def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

def print_hist(h):
    keys = sorted(h.keys())
    for key in keys:
        print(key, h[key])


h = histogram('brontosaurus')
print_hist(h)
