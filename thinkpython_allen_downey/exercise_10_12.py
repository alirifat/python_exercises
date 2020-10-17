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

def reverse_pair(words):
    reverses = []
    for word in words:
        if bisect(words, word[::-1]):
            reverses.append([word, word[::-1]])
    return reverses
