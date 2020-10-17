def longer_20(file):
    with open(file, 'r') as fin:
        words = fin.readlines()
    for word in words:
        if len(word.strip()) > 20:
            print(word.strip())

longer_20('words.txt')
