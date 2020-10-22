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

def swap_counts(word1, word2):
    if len(word1) != len(word2):
        return -1
    i = 0
    count = 0
    while i < len(word1):
        if word1[i] != word2[i]:
            count += 1
        i += 1
    return count



def metathesis(d):
    res = []
    for t in d.values():
        for word1 in t:
            for word2 in t:
                if word1 < word2 and swap_counts(word1, word2) == 2:
                    res.append((word1, word2))
    return res

d = anagrams_v1(words)

t = metathesis(d)
_ = [print(pair) for pair in t]
