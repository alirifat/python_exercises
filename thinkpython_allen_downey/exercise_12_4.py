with open('words.txt', 'r') as fin:
    lines = fin.readlines()
words = [line.strip() for line in lines]

def anagrams_v1(words):
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

def anagrams_v2(words):
    sorted_d = dict()
    d = anagrams_v1(words)
    for k, v in d.items():
        sorted_d[k] = (len(v), v)
    t = list(sorted_d.values())
    t.sort(reverse=True)
    return t

_ = [print(anagram) for anagram in anagrams_v2(words)]

def anagrams_v3(words):
    d = anagrams_v1(words)
    t = []
    for k, v in d.items():
        if len(k) == 8 and len(v) > 1:
            t.append((len(v), v))
    t.sort(reverse=True)
    return t

_ = [print(anagram) for anagram in anagrams_v3(words)]
