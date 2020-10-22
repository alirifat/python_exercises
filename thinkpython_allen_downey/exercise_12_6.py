with open('words.txt', 'r') as fin:
    lines = fin.readlines()
words = {line.strip():None for line in lines}
for letter in ['a', 'i', '']:
    words[letter] = None

def find_children(word, words):
    res = []
    i = 0
    while i < len(word):
        child = word[:i] + word[i+1:]
        if child in words:
            res.append(child)
        i += 1
    return res

known = dict()
known[''] = ['']

def check_reducibility(word, words):
    if word in known:
        return known[word]
    res = []
    for child in find_children(word, words):
        if check_reducibility(child, words):
            res.append(child)
    known[word] = res
    return res

res = []
for word in words:
    t = check_reducibility(word, words)
    if t != []:
        res.append((len(word), word))
res.sort(reverse=True)
longest_reducible_word = res[0][1]
print(longest_reducible_word)

def print_all_children(word, words):
    if word == '':
        return
    i = 0
    while i < len(word):
        w = word[:i] + word[i+1:]
        if w in words:
            res.append(w)
            word = w
            break
        i += 1
    print(word, end = ' ')
    return print_all_children(word, words)

print_all_children(longest_reducible_word, words)
