def is_abecedarian(word):
    i = 0
    while i < len(word) - 1:
        if not word[i] <= word[i+1]:
            return False
        i += 1
    return True

print(is_abecedarian('AEGILOPS'))
print(is_abecedarian('BILLOWY'))
print(is_abecedarian('computer'))
