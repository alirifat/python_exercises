def rotate_word(string, integer):
    rotated = ''
    for char in string:
        num = ord(char)
        if (num > 64) and (num < 91):
            new = ((num + (integer % 26)) % 91) % 65
            rotated += chr(65 + new)
        if (num > 96) and (num < 123):
            new = ((num + (integer % 26)) % 123) % 97
            rotated += chr(97 + new)
    return rotated

print(rotate_word('MELON', -10))
print(rotate_word('melon', -10))
print(rotate_word('cheer', 7))
