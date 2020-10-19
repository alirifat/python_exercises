import time
with open('words.txt', 'r') as fin:
    words = fin.readlines()

def words_append(words):
    list_words = []
    start = time.time()
    for word in words:
        list_words.append(word.strip())
    stop = time.time()
    return stop-start

def words_concatenate(words):
    list_words = []
    start = time.time()
    for word in words:
        list_words = list_words + [word.strip()]
    stop = time.time()
    return stop-start

print(words_append(words))
print(words_concatenate(words))
