with open('words.txt', 'r') as fin:
    lines = fin.readlines()
words = []
for line in lines:
    words.append(line.strip())

def bisect(words, target):
    if len(words) == 0:
        return False
    mid_value = len(words)//2
    if target == words[mid_value]:
        return True
    if target < words[mid_value]:
        return bisect(words[:mid_value], target)
    else:
        return bisect(words[mid_value+1:], target)

def two_way_interlock(words, word):
    return bisect(words, word[::2]) and bisect(words, word[1::2])

for word in words:
    if two_way_interlock(words, word):
        print(word, word[::2], word[1::2])

def three_way_interlock(words, word):
    return bisect(words, word[::3]) and bisect(words, word[1::3]) and \
           bisect(words, word[2::3])

for word in words:
    if three_way_interlock(words, word):
        print(word, word[::3], word[1::3], word[2::3])
