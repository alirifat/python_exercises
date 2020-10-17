def uses_only(word, letters):
    for letter in word:
        if not letter in letters:
            return False
    return True

print(uses_only('laptop', 'alopt'))
print(uses_only('computer', 'cemoprt'))

# generate a sentence-like with the given letters
def genererate_sentence(letters, length):
    from random import randint
    sentence = ''
    letters_with_space = letters + ' '
    for i in range(length):
        index = randint(0, len(letters))
        sentence += letters_with_space[index]
    return sentence

print(genererate_sentence('acefhlo', 10))
