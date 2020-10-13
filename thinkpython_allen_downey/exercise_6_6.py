def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print(middle('o'))
print(middle('oo'))
print(middle(''))
# calling middle with one or two letters returns an empty string.

def is_palindrome(word):
    if len(word) < 2:
        return True
    else:
        if first(word) == last(word):
            word = middle(word)
            return is_palindrome(word)
        return False

print(is_palindrome('noon'))
