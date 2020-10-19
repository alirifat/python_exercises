with open('words.txt', 'r') as fin:
    lines = fin.readlines()

words_dict = {}
for line in lines:
    word = line.strip()
    words_dict[word] = 0

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


import time
print('Test List')
start = time.time()
print('zymology' in words)
print(time.time() - start)
print('\nTest Dictionary Keys')
start = time.time()
print('zymology' in words_dict)
print(time.time() - start)
print('\nTest Bisection Search')
start = time.time()
print(bisect(words, 'zymology'))
print(time.time() - start)
