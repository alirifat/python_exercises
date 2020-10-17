def is_anagram(s1, s2):
    s1 = s1.strip(' ').lower()
    s2 = s2.strip(' ').lower()
    if len(s1) != len(s2):
        return False
    for c in s1:
        if not c in s2:
            return False
    return True

print(is_anagram('Debit Card', 'Bad Credit'))
print(is_anagram('act', 'cat'))
