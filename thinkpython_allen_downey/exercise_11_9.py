def has_duplicates(t):
    d = dict()
    for item in t:
        if item not in d:
            d.setdefault(item, True)
        else:
            return True
    return False

print(has_duplicates([1,2,3,4,5,6]))
